# fastapi_data_tool/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import upload, preprocess, visualize

app = FastAPI(title="Data Preprocessing & Visualization API")

# CORS settings for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(preprocess.router, prefix="/preprocess", tags=["Preprocess"])
app.include_router(visualize.router, prefix="/visualize", tags=["Visualize"])

@app.get("/")
def root():
    return {"message": "Welcome to the Data Preprocessing & Visualization API"}