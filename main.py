import os
from excel_reader import load_data
from birthday import get_today_birthdays
from telegram_sender import send_photo


TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
FILE_PATH = "xodimlar.xlsx"


def build_post(df):
    header = "🎊 Bugun jamoamizda kayfiyat ikki karra ko‘tarinki!\n\n"

    body = ""
    for i, (_, row) in enumerate(df.iterrows(), start=1):
        body += f"{i}) {row['Filial']} xodimi {row['FIO']}\n"

    footer = "\n🎂 Tug‘ilgan kuningiz muborak bo‘lsin 🌟"
    return header + body + footer


def main():
    df = load_data(FILE_PATH)
    birthdays = get_today_birthdays(df)

    if birthdays.empty:
        send_photo(TOKEN, CHAT_ID, "birthday.jpg", "Bugun tug‘ilganlar yo‘q 🎂")
        return

    post = build_post(birthdays)
    send_photo(TOKEN, CHAT_ID, "birthday.jpg", post)


if __name__ == "__main__":
    main()