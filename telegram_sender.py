import requests

def send_photo(token, chat_id, photo_path, caption):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"

    with open(photo_path, "rb") as photo:
        files = {"photo": photo}

        data = {
            "chat_id": chat_id,
            "caption": caption
        }

        response = requests.post(url, data=data, files=files)

        if response.status_code != 200:
            raise Exception(f"Telegram error: {response.text}")