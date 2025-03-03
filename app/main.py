from fastapi import FastAPI, File, UploadFile, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime, select
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime
import shutil
from fastapi.middleware.cors import CORSMiddleware

# FastAPI app
app = FastAPI()

# Enable CORS so the frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
DATABASE_URL = "mysql+pymysql://user:password@mysql-db:3306/mydatabase"  # Use 'mysql-db' as hostname inside Docker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Voice Recording Model
class VoiceRecording(Base):
    __tablename__ = "voice_recordings"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(engine)

# API Endpoints
@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running"}

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        file_location = f"uploads/{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Save file info in DB
        db = SessionLocal()
        new_record = VoiceRecording(filename=file.filename, filepath=file_location)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        db.close()

        return {"message": "File uploaded successfully", "file": new_record.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/uploaded-files/")
def get_uploaded_files():
    """Fetches a list of uploaded files from the database"""
    try:
        db: Session = SessionLocal()
        files = db.execute(select(VoiceRecording)).scalars().all()
        db.close()
        return [{"id": file.id, "filename": file.filename, "filepath": file.filepath} for file in files]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
