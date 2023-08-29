import requests
import concurrent.futures
import time

API_URL = "http://flaskapp:8000/"
NUM_REQUESTS = 50

def send_request(i):
    """Send a request to the API and return the response text."""
    start_time = time.time()
    response = requests.get(API_URL)
    total_time = time.time() - start_time
    time.sleep(0.01)
    return (total_time, response.text)

def main():
    # Use a ThreadPool to simulate multiple clients sending requests concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        responses = list(executor.map(send_request, range(NUM_REQUESTS)))
        end_time = time.time()

    print(f"Total Time: {end_time - start_time}")
    
    # Print the first 10 responses to verify
    for resp in responses[:10]:
        print(resp)

if __name__ == "__main__":
    main()
