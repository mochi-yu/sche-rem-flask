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
        # レコードを挿入
        sql = "INSERT INTO `GroupInformation` (`GroupID`, `GroupName`, `Author`, `StartDay`, `EndDay`, `StartHour`, `EndHour`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, ('ABCDEFGH','だんご４兄弟','CHIGIRI','8/16','8/26','9','23'))
 
    # コミットしてトランザクション実行
    connection.commit()

# 終了処理
cursor.close()
# connection.close()