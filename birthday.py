from datetime import datetime

def get_today_birthdays(df):
    today = datetime.today()

    birthdays = df[
        (df["Tug'ilgan_sana"].dt.day == today.day) &
        (df["Tug'ilgan_sana"].dt.month == today.month)
    ]

    return birthdays