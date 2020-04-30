import requests
import time

while True:
    time.sleep(0.1)
    try:
        url = "http://35.228.25.54"
        print(requests.get(f"{url}:5000/version").text)
    except:
        print("Not running")