import mysql.connector
from models.create_group_request_param import CreateGroupRequestParam
from models.group_info import GroupInfo
from setting import *

def _connectDB():
    # DBに接続
    cnx = mysql.connector.connect(
        database=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
    )

    if cnx.is_connected:
        print("database connected.")

    cursor = cnx.cursor(buffered=True, dictionary=True)

    return cursor, cnx


def init_db():
    try:
        cursor, cnx = _connectDB()

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
                    StartDate VARCHAR(255) NOT NULL,
                    EndDate VARCHAR(255) NOT NULL,
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
                    RefID int NOT NULL AUTO_INCREMENT,
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

def insert_group(newGroupInfo: CreateGroupRequestParam) -> GroupInfo:
    print()