import pandas as pd

import constant

# 内部資材
from lib import define_table
from lib.define_table import app, db  # Flaskアプリケーションをインポート

# 固定値
cons = constant.constant()


def select_t_post():
    """t_post：全件検索"""
    with app.app_context():
        t_post = define_table.t_post.query.all()
    return t_post


def select_t_post_bk():
    """t_post：全件検索"""
    with app.app_context():
        t_post = define_table.t_post_bk.query.all()
    return t_post


def delete_t_post():
    """t_post：全件削除"""
    with app.app_context():
        db.session.query(define_table.t_post).delete()
        transaction_commit()


def delete_t_post_bk():
    """t_post：全件削除"""
    with app.app_context():
        db.session.query(define_table.t_post_bk).delete()
        transaction_commit()


def backup_t_post():
    """t_post_bk：t_postのレコードをコピーする"""
    with app.app_context():
        t_post = select_t_post()
        for p in t_post:
            row = define_table.t_post_bk(
                p.post_date,
                p.post_seconds,
                p.post_milli_seconds,
                p.post_name,
                p.post_text,
            )
            # 登録
            db.session.add(row)
        # コミット
        transaction_commit()


def get_t_post():
    """t_post：リストで返却"""
    with app.app_context():
        t_post = select_t_post()
        coords = [
            [
                p.post_date,
                p.post_seconds,
                p.post_milli_seconds,
                p.post_name,
                p.post_text,
            ]
            for p in t_post
        ]
    return coords


def add_post(yyyymmdd, hhmmss, milliSeconds, nm, text):
    """書込を登録する"""
    with app.app_context():
        # 登録レコード作成
        row = define_table.t_post(yyyymmdd, hhmmss, milliSeconds, nm, text)
        # 登録
        db.session.add(row)
        # コミット
        transaction_commit()


def make_table_csv():
    """テーブルデータをcsv出力する"""
    with app.app_context():
        # t_post
        t_post = select_t_post()
        t_pos_list = []
        for p in t_post:
            add_list = []
            add_list.append(p.post_date)
            add_list.append(p.post_seconds)
            add_list.append(p.post_milli_seconds)
            add_list.append(p.post_name)
            add_list.append(p.post_text)
            t_pos_list.append(add_list)
        # データフレーム作成
        dt = pd.DataFrame(
            t_pos_list,
            columns=[
                "post_date",
                "post_seconds",
                "post_milli_seconds",
                "post_name",
                "post_text",
            ],
        )
        # csv出力
        dt.to_csv("t_post.csv", encoding="utf_8_sig", index=False)


def input_t_post_csv():
    """t_post.csvを取り込む"""
    with app.app_context():
        df = pd.read_csv("t_post.csv", dtype=str)
        for i in range(len(df)):
            post_date = df.iloc[i][0]
            post_seconds = df.iloc[i][1]
            post_milli_seconds = df.iloc[i][2]
            post_name = df.iloc[i][3]
            post_text = df.iloc[i][4]
            # 登録データ作成
            row = define_table.t_post(
                post_date, post_seconds, post_milli_seconds, post_name, post_text
            )
            # 登録
            db.session.add(row)
        # コミット
        transaction_commit()


def input_csv_table():
    """csvをテーブルに取り込む"""
    delete_t_post()
    input_t_post_csv()


def transaction_commit():
    """commit実施"""
    db.session.commit()
