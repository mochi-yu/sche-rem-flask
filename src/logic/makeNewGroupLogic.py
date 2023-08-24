from models.create_group_request_param import CreateGroupRequestParam
from models.group_info import GroupInfo
from database.GroupInformationTable import insert_group
from database.GroupUserTable import insert_group_users
import uuid

def make_new_group_logic(newGroup: CreateGroupRequestParam):
    groupID = str(uuid.uuid4())

    createdGroup = insert_group(newGroup, groupID)
    addedUsers = insert_group_users(newGroup.groupUsers, groupID)
    # print(addedUsers)

    createdGroup["groupUsers"] = newGroup.groupUsers
    createdGroup["schedules"] = []

    return GroupInfo(**createdGroup)