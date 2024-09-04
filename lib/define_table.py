import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# setting
from . import setting

settings = setting.setting()
DATABASE = settings.DATABASE
HOST = settings.HOST
PORT = settings.PORT
DBNAME = settings.DBNAME
USER = settings.USER
PASSWORD = settings.PASSWORD
SQLITE = settings.SQLITE
if SQLITE != "":
    # os.path.abspath は、指定された相対パスを絶対パスに変換する関数
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.abspath(SQLITE)}"
else:
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(
        DATABASE, USER, PASSWORD, HOST, PORT, DBNAME
    )


###########################################################
# dbインスタンスを作成
###########################################################
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# Unicodeエスケープの設定
app.config["JSON_AS_ASCII"] = False
db = SQLAlchemy(app)


###########################################################
# t_post定義
###########################################################
class t_post(db.Model):
    post_date = db.Column(db.String, primary_key=True)
    post_seconds = db.Column(db.String, primary_key=True)
    post_milli_seconds = db.Column(db.String, primary_key=True)
    post_name = db.Column(db.String)
    post_text = db.Column(db.Text)

    def __init__(
        self, post_date, post_seconds, post_milli_seconds, post_name, post_text
    ):
        self.post_date = post_date
        self.post_seconds = post_seconds
        self.post_milli_seconds = post_milli_seconds
        self.post_name = post_name
        self.post_text = post_text


###########################################################
# t_post_bk定義
###########################################################
class t_post_bk(db.Model):
    post_date = db.Column(db.String, primary_key=True)
    post_seconds = db.Column(db.String, primary_key=True)
    post_milli_seconds = db.Column(db.String, primary_key=True)
    post_name = db.Column(db.String)
    post_text = db.Column(db.Text)

    def __init__(
        self, post_date, post_seconds, post_milli_seconds, post_name, post_text
    ):
        self.post_date = post_date
        self.post_seconds = post_seconds
        self.post_milli_seconds = post_milli_seconds
        self.post_name = post_name
        self.post_text = post_text
