#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os

hbnb_storage_type = os.getenv('HBNB_TYPE_STORAGE')

class Review(BaseModel, Base):
    """ Review classto store review information """
    if hbnb_storage_type == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initializing the review object"""
        super().__init__(*args, **kwargs)
