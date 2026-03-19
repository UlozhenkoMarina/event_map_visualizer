from sqlalchemy.orm import Session
from typing import List, Optional
from backend.app.models.orm.events import Event as ORMEvent
from backend.app.models.schemas.events import EventCreate
from datetime import datetime

def create_event(db: Session, event: EventCreate):
    # db_event = ORMEvent(
    #     name=event.name,
    #     date=event.date,
    #     description=event.description,
    #     category=event.category
    # )
    db_event = ORMEvent(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events(db: Session, start_date: Optional[datetime] = None,
               end_date: Optional[datetime] = None,
               category: Optional[str] = None) -> List[ORMEvent]:
    query = db.query(ORMEvent)
    if start_date:
        query = query.filter(ORMEvent.date >= start_date)
    if end_date:
        query = query.filter(ORMEvent.date <= end_date)
    if category:
        query = query.filter(ORMEvent.category == category)
    return query.all()