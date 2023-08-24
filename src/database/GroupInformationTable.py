from models.create_group_request_param import CreateGroupRequestParam
from models.group_info import GroupInfo
from database.db import _connectDB

def insert_group(newGroup: CreateGroupRequestParam, groupID: str):
    createdGroup = None
    try:
      cursor, cnx = _connectDB()

      sql = ('''
        INSERT INTO GroupInformation
        (GroupID, GroupName, Author, StartDate, EndDate, StartHour, EndHour)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
      ''')

      cursor.execute(sql, (
          groupID,
          newGroup.groupName,
          newGroup.author,
          newGroup.startDate,
          newGroup.endDate,
          newGroup.startHour,
          newGroup.endHour,
      ))

      cnx.commit()

      sql = '''
        SELECT * FROM GroupInformation
        WHERE groupID = %s;
      '''

      cursor.execute(sql, (groupID, ))
      createdGroup = cursor.fetchall()[0]

    except Exception as e:
      print(f"Error in insert_group(): {e}")

    finally:
      cursor.close()
      if cnx is not None and cnx.is_connected:
        cnx.close()
    
    return createdGroup
