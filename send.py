import os

import requests

msg = "hello:)"
url = os.environ.get("webhook_url")
data = {"content": msg}


def main():
    requests.post(url, data)


if __name__ == "__main__":
    main()
