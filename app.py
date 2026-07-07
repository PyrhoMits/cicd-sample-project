import requests


def fetch_status(url: str) -> int:
    """Return the HTTP status code for a URL."""
    response = requests.get(url, timeout=5)
    return response.status_code


if __name__ == "__main__":
    print(fetch_status("https://example.com"))
