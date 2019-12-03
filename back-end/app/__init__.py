from configparser import ConfigParser
from os import path

from flask import Flask
import pymysql


fp = path.join('.', 'conf.ini')
conf = ConfigParser()
conf.read(fp)
user = conf.get('automobile', 'user')
passwd = conf.get('automobile', 'passwd')
host = conf.get('automobile', 'host')
port = conf.get('automobile', 'port')
db = conf.get('automobile', 'db')

db = pymysql.connect(host, user, passwd, db, int(port), autocommit=True)
cursor = db.cursor(pymysql.cursors.DictCursor)

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    from .automobile import automobile_blueprint
    app.register_blueprint(automobile_blueprint)

    return app
