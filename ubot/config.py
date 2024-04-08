# -*- encoding: utf-8 -*-
"""Config vars module"""
import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    ApiId = os.environ.get('API_ID')
    ApiHash = os.environ.get('API_HASH', None)
    TokenBot = os.environ.get('BOT_TOKEN', None)
    #log_group = int(os.environ.get('LOG_GROUP', False))
    #mongodb = os.environ.get('MONGODB')