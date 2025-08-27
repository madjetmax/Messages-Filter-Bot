from sqlalchemy import DateTime, Float, String, Text, Boolean, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import * 
import datetime
from zoneinfo import ZoneInfo

base_time_zone =  datetime.timezone.utc #ZoneInfo(MODELS_TIME_ZONE)

def now() -> datetime.datetime:
    date = datetime.datetime.now(base_time_zone)
    return date

class Base(DeclarativeBase):
    created: Mapped[datetime.datetime] = mapped_column(DateTime(True), default=now)
    updated: Mapped[datetime.datetime] = mapped_column(DateTime(True), default=now, onupdate=now)
    
class Keyword(Base):
    __tablename__ = "trigger_keywords"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    word: Mapped[str] = mapped_column(String(255))

class TriggerName(Base):
    __tablename__ = "trigger_names"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))

class Phrase(Base):
    __tablename__ = "trigger_phrases"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text)