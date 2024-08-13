import time


class MotorControl:
    def __init__(self):
        self.is_active = False

    def move(self) -> bool:
        self.is_active = True
        # print("start moving motor")
        time.sleep(2)
        # print("stop moving motor")
        self.is_active = False
        return True
