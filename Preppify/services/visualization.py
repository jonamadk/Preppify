import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import base64

def plot_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()

def histogram(df: pd.DataFrame, column: str):
    fig = plt.figure()
    df[column].hist()
    return plot_to_base64(fig)

def correlation_heatmap(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    return plot_to_base64(fig)

def scatter_plot(df: pd.DataFrame, x: str, y: str):
    fig = plt.figure()
    sns.scatterplot(x=df[x], y=df[y])
    return plot_to_base64(fig)
