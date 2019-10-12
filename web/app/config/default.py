import os
import json

class Config():
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 9090
    HTML_MINIFY = True
    SECRET_KEY = 'EG_Education_development_key'
    # 针对Pymongo3.9 mongoengine0.18.2 验证添加
    MONGODB_SETTINGS = {
        'db': 'KG_Education',
        'host': '127.0.0.1',
        'port': 27017,
        'username': 'root',
        'password': 'root1234',
        'authentication_source':'admin'
    }
    
