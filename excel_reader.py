import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path)
    df["Tug'ilgan_sana"] = pd.to_datetime(df["Tug'ilgan_sana"], errors="coerce")
    return df