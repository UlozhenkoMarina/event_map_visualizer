from pydantic import BaseModel, PositiveInt, Optional
from datetime import datetime

class EventBase(BaseModel):
    name: str
    date: datetime
    description: Optional[str] = None
    category: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class EventCreate(EventBase):
    pass

class EventRead(EventBase):
    id: PositiveInt