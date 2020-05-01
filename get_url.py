import requests
import time

while True:
    time.sleep(0.1)
    try:
        url = ""
        print(requests.get(f"{url}:5000/version").text)
    except:
        print("Not running")