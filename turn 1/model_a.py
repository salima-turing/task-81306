import time
import concurrent.futures

# Simple audio processing function (replace this with your actual audio processing logic)
def process_audio(data):
	time.sleep(0.1) # Simulate processing time
	return len(data)

def load_test(num_requests, workers):

	test_data = [b'some audio data' for _ in range(num_requests)] # Replace with actual audio data or generate random data

	start_time = time.time()

	with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
		results = executor.map(process_audio, test_data)

	duration = time.time() - start_time

	print(f"Load Test Results:")
	print(f"-----------------")
	print(f"Number of requests: {num_requests}")
	print(f"Number of workers: {workers}")
	print(f"Execution time: {duration:.2f} seconds")
	print(f"Requests per second: {num_requests / duration:.2f}")

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description="Audio Processing Load Test")
	parser.add_argument('-n', '--num-requests', type=int, default=100, help="Number of requests to send")
	parser.add_argument('-w', '--workers', type=int, default=10, help="Number of worker threads")
	args = parser.parse_args()

	load_test(num_requests=args.num_requests, workers=args.workers)
