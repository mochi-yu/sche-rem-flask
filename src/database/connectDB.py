# python-dotenvを使って環境変数を設定するためのコードです。

import os
import mysql.connector
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からデータベース接続情報を取得する
db_name = os.getenv("DB_NAME")
user_name = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
db_host = os.getenv("HOST")

try:
    # データベースに接続
    connection = mysql.connector.connect(
        host=db_host,
        user=user_name,
        password=password,
        database=db_name
    )

    if connection.is_connected():
        print("データベースに接続しました。")

    # ここでデータベース操作を行うことができます
    cur = connection.cursor()
    # SQL
    cur.execute("select * from GroupInformation")
    # 列毎に集計
    for row in cur:
        print("%s, %s, %s, %s, %s, %d, %d" % 
            (row[0], row[1], row[2], row[3], row[4], row[5], row[6])) #%dはInteger型

    connection.commit()

except mysql.connector.Error as err:
    print(f"エラー: {err}")
finally:
    # データベース接続をクローズ
    if 'connection' in locals():
        connection.close()
        print("データベース接続をクローズしました。")
