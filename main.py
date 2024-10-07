from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from db import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)