import requests
import csv
from datetime import datetime

urls = [
    "https://google.com",
    "https://github.com",
    "https://fakesite123456789.com"
]
log_file = "status_log.csv"

def check_url(url):
    try:
        response = requests.get(url, timeout = 5)
        status_code = response.status_code
        response_time = round(response.elapsed.total_seconds(), 2)
        result = "UP" if status_code == 200 else "DOWN"
        print(f"{url} - Status {status_code} - {response_time}s - {result}")
        return status_code, response_time, result
    
    except requests.exceptions.RequestException as e:
        print(f"{url} - ERROR: could not connect - DOWN")
        return "N/A", "N/A", "DOWN"

def main():
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["url", "status_code", "response_time", "result", "timestamp"])

        for url in urls:
            status_code, response_time, result = check_url(url)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([url, status_code, response_time, result, timestamp])

if __name__=="__main__":
    main()