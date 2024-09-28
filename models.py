from sqlalchemy import create_engine, Column, Integer, DateTime, String, LargeBinary, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import UUID

Base = declarative_base()


class Video(Base):
    __tablename__ = 'Video'
    uuid = Column(UUID, primary_key=True)
    upload_date = Column(DateTime)
    content_hash = Column(LargeBinary)
    is_duplicate = Column(Boolean)
    duplicate_for = Column(UUID)
    is_hard = Column(Boolean)
