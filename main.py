import ray

from actors.CameraMotorActor import CameraMotorActor
from actors.StackingActor import StackingActor
from actors.PredictionActor import PredictionActor

ray.init() # Only call this once.

# Helper function to check if a task is completed
def task_completed(task_ref: ray.ObjectRef):
    if task_ref is None:
        return False
    ready_refs, _ = ray.wait([task_ref], timeout=0)
    return len(ready_refs) > 0


# Main function that runs the ray workflow. This function will be called by the workflow engine to start the workflow execution.
# The workflow engine will be responsible for managing the execution of tasks and their dependencies.
def run():
    current_stacking_task = None

    # Instantiate the actors
    camera_motor_actor = CameraMotorActor.remote()
    stacking_actor = StackingActor.remote()
    prediction_actor = PredictionActor.remote()

    # Start z-position task sequentially
    z_positions = ray.get(camera_motor_actor.find_best_z.remote())
    cur_z_position = z_positions[0]

    # The stack will keep track of the number of completed 60 image batches to know how many stacking tasks need to be run
    batched_images_stack = []

    # Take the first batch of 60 images for the first z-position (async)
    current_image_task = camera_motor_actor.take_images_task.remote(cur_z_position)

    idx = 1
    while True:
        # get the current z_position
        if idx < len(z_positions):
            cur_z_position = z_positions[idx]

        # If all tasks have successfully completed, terminate the loop and continue
        if idx >= len(z_positions) and \
                len(batched_images_stack) == 0 and \
                current_stacking_task is not None and \
                task_completed(current_stacking_task):
            break

        # If a batch of 60 images is taken, start a new one
        if current_image_task is not None and task_completed(current_image_task):
            batched_images_stack.append(True)
            if idx < len(z_positions):
                current_image_task = camera_motor_actor.take_images_task.remote(cur_z_position)
                idx += 1
            else:
                current_image_task = None

        # if previous images already exist, start the stacking process if currently none is running
        if len(batched_images_stack) > 0:
            if current_stacking_task is None or task_completed(current_stacking_task):
                current_stacking_task = stacking_actor.stacking_task.remote()
                batched_images_stack.pop()

    # once all stackings are completed, start prediction task
    prediction_actor.predict.remote()

if __name__ == "__main__":
    run()
