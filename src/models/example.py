#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple database model example that captures some generic data.
"""

from db.database import Base
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime

class Example(Base):

    __tablename__ = 'example'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    flag = Column(Boolean, nullable=False, default=False)
    data = Column(String)
    
    def __init__(self, **k):
        self.id = k['id']
        self.created_at = k['created_at']
        self.updated_at = k['updated_at']
        self.flag = k['flag']
        self.data = k['data']

    def __repr__(self):
        return f'<Example {self.updated_at} :: {self.data}'


