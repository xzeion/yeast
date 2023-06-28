#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, Response

root = Blueprint('root', __name__)

@root.route('/', methods=['GET'])
def page_root():
    return Response('Hello Flask World!')
