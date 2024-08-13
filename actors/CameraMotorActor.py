import ray
from core.camera_control import CameraControl
from core.motor_control import MotorControl


@ray.remote
class CameraMotorActor:
    def __init__(self):
        self.motor_control = MotorControl()
        self.camera_control = CameraControl()

    def find_best_z(self):
        for i in range(1):
            print(f"Moving motor and taking image {i + 1}/1")
            self.motor_control.move()
            self.camera_control.take_image()
        print(f"find_best_z done")
        return [0, 1, 2]


    def take_images_task(self, z_position: float):
        for i in range(10):
            print(f"Moving motor and taking image {i + 1}/10")
            self.motor_control.move()
            self.camera_control.take_image()
        print(f"take_image_task done")