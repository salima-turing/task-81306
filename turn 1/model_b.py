from locust import HttpUser, TaskSet, task, between
# import speech_recognition as sr
import random
import time

# Function to simulate audio processing
def process_audio():
    # Replace this with your actual audio processing logic or a call to your Python program
    # For demonstration, we'll use a random sleep time to simulate processing time.
    processing_time = random.uniform(0.5, 2.0)
    time.sleep(processing_time)

class AudioProcessingUser(HttpUser):
    wait_time = between(0.5, 1.5)  # Time to wait between requests

    class UserBehavior(TaskSet):
        @task
        def process_audio_file(self):
            # Here, you can call your actual audio processing function or script
            process_audio()
