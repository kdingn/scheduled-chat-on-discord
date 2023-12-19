import os

import requests

msg = "hello:)"
url = os.environ.get("WEBHOOK_URL")
data = {"content": msg}


def main():
    requests.post(url, data)


if __name__ == "__main__":
    main()
