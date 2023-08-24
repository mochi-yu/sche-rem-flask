import mysql.connector
from models.create_group_request_param import CreateGroupRequestParam
from models.group_info import GroupInfo
from setting import *

def _connectDB(isDict = True):
    # DBに接続
    cnx = mysql.connector.connect(
        database=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
    )

    if cnx.is_connected:
        print("database connected.")

    cursor = cnx.cursor(buffered=True, dictionary=isDict)

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
                    groupID VARCHAR(255) NOT NULL,
                    groupName VARCHAR(255) NOT NULL,
                    author VARCHAR(255) NOT NULL,
                    startDate VARCHAR(255) NOT NULL,
                    endDate VARCHAR(255) NOT NULL,
                    startHour int NULL,
                    endHour int NULL,
                    PRIMARY KEY (groupID)
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
                    refID int NOT NULL AUTO_INCREMENT,
                    groupID VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
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