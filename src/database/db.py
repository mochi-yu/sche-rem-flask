import mysql.connector
from setting import *

cnx = None

def init_db():
    try:
        # DBに接続
        cnx = mysql.connector.connect(
            database=MYSQL_DATABASE,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
        )

        if cnx.is_connected:
            print("database connected.")

        cursor = cnx.cursor(buffered=True)


        # GroupInformationデーブルの初期化
        try:
            # GroupInformationテーブルがあるかの問い合わせ
            sql = '''
                SELECT * FROM GroupInformation LIMIT 1;
            '''
            cursor.execute(sql)
            print("GroupInformationテーブルがありました。")
        except Exception as e:
            print("GroupInformationテーブルがありませんでした。")

            # GroupInformationテーブルの作成
            sql = '''
                CREATE TABLE GroupInformation (
                    GroupID VARCHAR(255) NOT NULL,
                    GroupName VARCHAR(255) NOT NULL,
                    Author VARCHAR(255) NOT NULL,
                    StartDay VARCHAR(255) NOT NULL,
                    EndDay VARCHAR(255) NOT NULL,
                    StartHour int NULL,
                    EndHour int NULL,
                    PRIMARY KEY (GroupID)
                );
            '''
            cursor.execute(sql)
            print("GroupInformationテーブルを作成しました。")


        # PerticipantInformationテーブルの初期化
        try:
            # PerticipantInformationテーブルがあるかの問い合わせ
            sql = '''
                SELECT * FROM PerticipantInformation LIMIT 1;
            '''
            cursor.execute(sql)
            print("PerticipantInformationテーブルがありました。")
        except Exception as e:
            print("PerticipantInformationテーブルがありませんでした。")

            # GroupInformationテーブルの作成
            sql = '''
                CREATE TABLE PerticipantInformation (
                    RefID VARCHAR(255) NOT NULL,
                    GroupID VARCHAR(255) NOT NULL,
                    Email VARCHAR(255) NOT NULL,
                    PRIMARY KEY (RefID)
                );
            '''
            cursor.execute(sql)
            print("PerticipantInformationテーブルを作成しました。")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cnx is not None and cnx.is_connected:
            cnx.close()

