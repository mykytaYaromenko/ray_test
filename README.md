# Ray Framework Testing

This repository is dedicated to examining [Ray](https://docs.ray.io/en/latest/), a framework for distributed computing, to understand the intricacies of constructing complex task workflows and to assess its performance.

## Configuration

1. Install the Ray library: `pip install -U "ray[default]"`
2. run `main.py`

## Functionality

Ray is a distributed computing framework that simplifies the writing of scalable and distributed programs. It revolves around two primary concepts: [Tasks](https://docs.ray.io/en/latest/walkthrough.html#remote-functions-tasks) and [Actors](https://docs.ray.io/en/latest/walkthrough.html#actors-tasks-with-state).

- Tasks: Stateless functions that can be executed in parallel. They are the fundamental execution unit in Ray.
- Actors: Stateful objects capable of executing tasks. They can maintain mutable state and are useful for encapsulating complex behavior.

Ray monitors tasks and actors, tracking their execution state, completion status (success, failure, cancellation), and completion time. It also supports defining retry policies, result caching, and more.

## Workflow Overview

The workflow outlined in this repository is a simple, mocked demonstration of a workflow, showcasing Ray's orchestration capabilities.

1. Retrieve z-positions: A task is initiated to obtain the z-positions for image capture.
2. Image Capture: Concurrently, batches of images for each of the three stripes are captured.
3. Image Stacking: As soon as a batch is completed, images are stacked.
4. Prediction: After image capture and stacking, a prediction task is executed.

The stacking task includes a simulated stress test to evaluate if full CPU utilization affects the flow's performance or causes crashes—none were observed. Runs can be started directly from code and begin instantly. New tasks are initiated within less than a second. Therefore, I don't think performance of the framework needs to be a concern.

## Conclusion
Ray is a powerful framework for distributed computing, offering a simple and intuitive API for constructing complex task workflows. It provides a wide range of features, including task monitoring, actor management, and fault tolerance, making it an excellent choice for building scalable and distributed applications.
