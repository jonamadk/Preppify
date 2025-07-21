import pandas as pd
import os

UPLOAD_PATH = "data/uploaded.csv"
PROCESSED_PATH = "data/processed.csv"

def save_uploaded_file(file, path=UPLOAD_PATH):
    df = pd.read_csv(file)
    df.to_csv(path, index=False)
    return df

def load_data(path=UPLOAD_PATH):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        raise FileNotFoundError(f"{path} does not exist")

def save_processed_data(df, path=PROCESSED_PATH):
    df.to_csv(path, index=False)
    return path
