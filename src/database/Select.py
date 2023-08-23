import pymysql.cursors
 
# データベースに接続
connection = pymysql.connect(host='ScheRem-mysql',
                             port=3306,
                             user='flask',
                             password='flask',
                             database='flask-mysql',
                             cursorclass=pymysql.cursors.DictCursor)
 
with connection:
    with connection.cursor() as cursor:
        # データ読み込み
        sql = "SELECT `GroupID`, `GroupName`, `Author`, `StartDay`, `EndDay`, `StartHour`, `EndHour` FROM `GroupInformation` WHERE `GroupID`=%s"
        cursor.execute(sql, ('ABCDEFGH'))
        result = cursor.fetchone()
        print(result)

# 終了処理
cursor.close()