from database.db import _connectDB

def insert_group_users(groupUsers: list[str], groupID: int) -> None:
    cursor, cnx = _connectDB()

    sql = '''
      INSERT INTO PerticipantInformation
      (GroupID, Email)
      VALUES (%s, %s)
    '''

    insertData = []
    for user in groupUsers:
        insertData.append((groupID, user))
    
    cursor.executemany(sql, insertData)
    cnx.commit()

    
    sql = '''SELECT * FROM PerticipantInformation WHERE groupID = %s'''
    cursor.execute(sql, (groupID, ))
    addedUsers = cursor.fetchall()
    
    cursor.close()
    cnx.close()

    return addedUsers

def get_users(groupID):
    cursor, cnx = _connectDB()

    sql = '''SELECT * FROM PerticipantInformation WHERE groupID = %s'''
    cursor.execute(sql, (groupID, ))
    users = cursor.fetchall()
    
    cursor.close()
    cnx.close()

    return users
