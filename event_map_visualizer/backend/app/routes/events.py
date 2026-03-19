from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from backend.app.database.session import get_db
from backend.app.models.schemas.events import EventCreate, EventRead
from backend.app.crud.events import create_event, get_events

router = APIRouter()

@router.get("/", response_model = List[EventRead])
def read_events(
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return get_events(db, start_date = start_date, end_date = end_date, category = category)

@router.post("/", response_model = EventRead)
def add_event(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)