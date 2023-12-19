import os

import requests

msg = "hello guys :)"
url = os.environ.get("WEBHOOK_URL")
data = {"content": msg}


def main():
    print("wwwwwwwwwwwwwwwwwwww")
    print(url)
    print("wwwwwwwwwwwwwwwwwwww")
    requests.post(url, data)


if __name__ == "__main__":
    main()
