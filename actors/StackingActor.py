import ray
from core.stacking import stack_images


@ray.remote
class StackingActor:
    def __init__(self):
        self.stacking_size = 60

    def stacking_task(self):
        print("Stacking images...")
        stack_images()
        print("stacking_task done")