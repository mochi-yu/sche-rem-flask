import pymysql.cursors
 
# データベースに接続
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='ckmr1226',
                             database='ScheRem',
                             cursorclass=pymysql.cursors.DictCursor)
 
with connection:
    with connection.cursor() as cursor:
        # データ読み込み
        sql = "SELECT 'GroupID', 'GroupName', 'Author', 'StartDay', 'EndDay', 'StartHour', 'EndHour' FROM `GroupInformation` WHERE `GroupID`=%s"
        cursor.execute(sql, ('ABCDEFG'))
        result = cursor.fetchone()
        print(result)