#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db.database import init_db
from flask import Flask, Response
from views.root import root
import logging

app = Flask(__name__)
app.register_blueprint(root)
app.config['BUNDLE_ERRORS'] = True

logging.basicConfig(
    level=logging.DEBUG,
    format = f'%(levelname)s: %(message)s'
)
log = logging.getLogger()

init_db()
