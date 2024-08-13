import math
import multiprocessing
import time


# crunch some numbers to simulate stacking process
def _generate_cpu_load(interval=30, utilization=95):
    "Generate a utilization % for a duration of interval seconds"
    start_time = time.time()
    for i in range(0, int(interval)):
        while time.time() - start_time < utilization / 100.0:
            a = math.sqrt(64 * 64 * 64 * 64 * 64)
        time.sleep(1 - utilization / 100.0)
        start_time += 1


def stack_images():
    print("start stacking")
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=_generate_cpu_load)
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    print(f"end stacking")
    return 99999


if __name__ == "__main__":
    processes = []
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=_generate_cpu_load)
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
