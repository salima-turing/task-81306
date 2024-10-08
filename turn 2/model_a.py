import time
import concurrent.futures
import argparse
import psutil

def process_audio(data):
    time.sleep(0.1)
    return len(data)


def load_test(num_requests, workers, ramp_up_time, ramp_up_step):
    test_data = [b'some audio data' for _ in range(num_requests)]

    start_time = time.time()
    current_requests = 0
    total_workers = workers

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(0, num_requests, ramp_up_step):
            # Ramp up the number of workers gradually
            if current_requests + ramp_up_step <= total_workers:
                current_workers = ramp_up_step
            else:
                current_workers = total_workers - current_requests

            current_requests += current_workers

            results = executor.map(process_audio, test_data[i:i + current_workers])

            process = psutil.Process()
            cpu_percent = process.cpu_percent(interval=1)
            memory_info = process.memory_info()
            print(f"CPU Usage: {cpu_percent}%")
            print(f"Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB")

            time.sleep(1)  # Control the ramp-up rate

    duration = time.time() - start_time

    print(f"Load Test Results:")
    print(f"-----------------")
    print(f"Number of requests: {num_requests}")
    print(f"Max Workers: {workers}")
    print(f"Ramp-up time: {ramp_up_time} seconds")
    print(f"Ramp-up step: {ramp_up_step}")
    print(f"Execution time: {duration:.2f} seconds")
    print(f"Requests per second: {num_requests / duration:.2f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audio Processing Load Test")
    parser.add_argument('-n', '--num-requests', type=int, default=100, help="Number of requests to send")
    parser.add_argument('-w', '--workers', type=int, default=10, help="Maximum number of worker threads")
    parser.add_argument('-r', '--ramp-up-time', type=int, default=10, help="Ramp-up time in seconds")
    parser.add_argument('-s', '--ramp-up-step', type=int, default=5, help="Number of requests to add per ramp-up step")
    args = parser.parse_args()

    load_test(num_requests=args.num_requests, workers=args.workers, ramp_up_time=args.ramp_up_time,
              ramp_up_step=args.ramp_up_step)
