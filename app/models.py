from sqlalchemy import Column, Integer, String, Boolean
from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.dialects.postgresql import ARRAY


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