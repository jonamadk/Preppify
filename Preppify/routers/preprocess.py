from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter()
DATA_PATH = "data/uploaded.csv"
PROCESSED_PATH = "data/processed.csv"

@router.post("/missing")
def handle_missing(strategy: str = "mean"):
    df = pd.read_csv(DATA_PATH)
    for col in df.columns:
        if df[col].isnull().any():
            if strategy == "mean" and df[col].dtype != "object":
                df[col].fillna(df[col].mean(), inplace=True)
            elif strategy == "median" and df[col].dtype != "object":
                df[col].fillna(df[col].median(), inplace=True)
            elif strategy == "mode":
                df[col].fillna(df[col].mode()[0], inplace=True)
            elif strategy == "drop":
                df.dropna(inplace=True)
    df.to_csv(PROCESSED_PATH, index=False)
    return {"message": f"Missing values handled using {strategy} strategy"}

@router.post("/encode")
def encode_data(method: str = "onehot"):
    df = pd.read_csv(PROCESSED_PATH)
    if method == "onehot":
        df = pd.get_dummies(df)
    elif method == "label":
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for col in df.select_dtypes(include="object").columns:
            df[col] = le.fit_transform(df[col])
    df.to_csv(PROCESSED_PATH, index=False)
    return {"message": f"Categorical data encoded using {method}"}

@router.post("/normalize")
def normalize_data(method: str = "minmax"):
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    df = pd.read_csv(PROCESSED_PATH)
    num_cols = df.select_dtypes(include="number").columns
    if method == "minmax":
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])
    df.to_csv(PROCESSED_PATH, index=False)
    return {"message": f"Numerical data normalized using {method}"}

@router.post("/save")
def save_data():
    return {"message": "Preprocessed data saved", "path": PROCESSED_PATH}
