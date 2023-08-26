from models.create_group_request_param import CreateGroupRequestParam
from models.group_info import GroupInfo
from database.GroupInformationTable import insert_group
from database.GroupUserTable import insert_group_users
from logic.sendEmailLogic import send_emails
import uuid

def make_new_group_logic(newGroup: CreateGroupRequestParam):
    groupID = str(uuid.uuid4())

    createdGroup = insert_group(newGroup, groupID)
    addedUsers = insert_group_users(newGroup.groupUsers, groupID)
    # print(addedUsers)

    # 参加者にメールを送る
    mailTitle = "新しい日程調整が作成されました。"
    mailBody = """
新しい日程調整が作成されました。
以下のリンクからあなたの日程調整を入力してください。
URL：https://sche-rem.vercel.app/email/{groupID}
    """
    send_emails(newGroup.groupUsers, mailTitle, mailBody)

    createdGroup["groupUsers"] = newGroup.groupUsers
    createdGroup["schedules"] = []

    return GroupInfo(**createdGroup)