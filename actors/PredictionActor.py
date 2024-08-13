import time
import ray
from random import randint
@ray.remote
class PredictionActor:
    def __init__(self):
        self.model_to_predict = "model"

    def predict(self):
        print("Predict image...")
        time.sleep(10)
        print("predict image done")
