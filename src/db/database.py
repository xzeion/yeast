#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ as env
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

engine = create_engine(
    f'postgresql://{env.get("DBUSER")}:{env.get("POSTGRES_PASSWORD")}@{env.get("HOST")}/{env.get("DBNAME")}',
    client_encoding='utf-8',
    echo=False
)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so
    # they will be registered properly on the metadata. Otherwise
    # you will have to import them first before calling init_db()
    if not database_exists(engine.url):
        create_database(engine.url)

    from models import example
    Base.metadata.create_all(bind=engine)
