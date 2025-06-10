from sqlalchemy import Column, Integer, String, Boolean, Text, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime


class Mushroom(Base):
    __tablename__ = "mushrooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    other_common_names = Column(ARRAY(String), nullable=True)
    scientific_name = Column(String)
    description = Column(String)
    home_photo_path = Column(String)
    location = Column(String)
    is_edible = Column(Boolean, default=False)
    source_url = Column(Text)
    # Optional relationship
    # photos = relationship("MushroomPhoto", backref="mushroom", cascade="all, delete")


class MushroomPhoto(Base):
    __tablename__ = "mushroom_photos"

    id = Column(Integer, primary_key=True)
    mushroom_id = Column(Integer, ForeignKey("mushrooms.id", ondelete="CASCADE"), index=True)
    where_found = Column(String)
    habitat = Column(String)
    resolution = Column(String)
    photo_path = Column(String, nullable=False)
    source_url = Column(Text)
    photographer = Column(String)
    upload_date = Column(DateTime, default=datetime.utcnow)
    camera_model = Column(String)
    lens = Column(String)
    aperture = Column(String)
    shutter_speed = Column(String)
    iso = Column(String)
    notes = Column(Text)
    season = Column(String)
    date_taken = Column(Date)
    verified = Column(Boolean, default=False)
    user_id = Column(Integer)  # FK to users later
    is_featured = Column(Boolean, default=False)
    alt_text = Column(Text)
    rating = Column(Integer, default=0)
    tags = Column(ARRAY(Text))
