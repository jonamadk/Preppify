from fastapi import APIRouter, UploadFile, File
import pandas as pd
import os

router = APIRouter()
DATA_DIR = "data"
DATA_PATH = os.path.join(DATA_DIR, "sample_data.csv")

# ✅ Make sure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

@router.post("/file")
async def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df.to_csv(DATA_PATH, index=False)
    return {"message": "File uploaded successfully", "columns": df.columns.tolist()}

@router.get("/preview")
async def preview_data():
    df = pd.read_csv(DATA_PATH)
    return df.head(10).to_dict(orient="records")

@router.get("/schema")
async def get_schema():
    df = pd.read_csv(DATA_PATH)
    dtypes = df.dtypes.apply(lambda x: str(x)).to_dict()
    missing = df.isnull().sum().to_dict()
    return {"dtypes": dtypes, "missing_values": missing}
