from fastapi import APIRouter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io
import base64

router = APIRouter()
DATA_PATH = "data/processed.csv"

def generate_plot(plt):
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

@router.get("/histogram")
def histogram(column: str):
    df = pd.read_csv(DATA_PATH)
    plt.figure()
    df[column].hist()
    return {"image": generate_plot(plt)}

@router.get("/correlation")
def correlation():
    df = pd.read_csv(DATA_PATH)
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    return {"image": generate_plot(plt)}

@router.get("/scatter")
def scatter(x: str, y: str):
    df = pd.read_csv(DATA_PATH)
    plt.figure()
    sns.scatterplot(x=df[x], y=df[y])
    return {"image": generate_plot(plt)}
