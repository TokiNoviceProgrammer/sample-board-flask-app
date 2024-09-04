# 内部資材
from define_table import app, db

###########################################################
# テーブルの作成実行
###########################################################
# アプリケーションコンテキストを作成して、その中でデータベース操作を行う
with app.app_context():
    db.drop_all()
    db.create_all()
    print("Tables created successfully")
