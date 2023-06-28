#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from db.database import init_db
import os

if __name__ == "__main__":
    init_db()
    app.run(
        host='0.0.0.0',
        threaded=True,
        debug=os.environ.get('DEBUG', False)
    )

