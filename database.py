from sqlmodel import Field, SQLModel
from datetime import datetime

class Topic(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    timestamp: datetime = Field(default_factory=datetime.now)