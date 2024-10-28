import time

import requests


def fetch_data(url):
    print(f"Fetching data from {url}")
    result = requests.get(url)
    return result


def main():
    urls = ["https://github.com/", "https://python.org/"] * 50
    results = []
    start = time.time()
    for url in urls:
        result = fetch_data(url)
        results.append(result)
    end = time.time()
    print(results)
    print(end - start)


if __name__ == "__main__":
    main()
