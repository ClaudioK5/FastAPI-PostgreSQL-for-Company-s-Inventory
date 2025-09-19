from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine, Base
Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/inventory/", response_model=schemas.InventoryItem)
def create_inventoryitem(inventoryitem: schemas.InventoryItemCreate, db: Session = Depends(get_db)):

    db_inventoryitem = models.InventoryItem(**inventoryitem.dict())
    db.add(db_inventoryitem)
    db.commit()
    db.refresh(db_inventoryitem)
    return db_inventoryitem

@app.get("/inventory/", response_model=List[schemas.InventoryItem])
def read_purchases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.InventoryItem).offset(skip).limit(limit).all()

@app.get("/")
def read_root():
    return {"message": "FastAPI is working"}

