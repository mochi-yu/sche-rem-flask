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
        # データ削除
        sql = "DELETE FROM `GroupInformation` WHERE `GroupID` = %s"
        cursor.execute(sql, ('ABCDEFGH'))
        connection.commit()
        print(cursor.rowcount, 'rows deleted')

# 終了処理
cursor.close()