from models.submit_group_request_param import SubmitGroupRequestParam
from models.group_info import GroupInfo
from logic.getGroupInfoLogic import get_group_info_with_groupID_logic
from database.GroupUserTable import get_users
from database.ScheduleInfoTable import insert_schedule
from logic.sendEmailLogic import send_emails

def submit_schedule_logic(requestParam: SubmitGroupRequestParam, groupID: str) -> GroupInfo:
    # 対象のユーザのrefIDを探す
    userRefID = 0

    groupUsers = get_users(groupID)
    requestParam.userMailAddress = requestParam.userMailAddress.replace("%40", "@")

    print(requestParam.userMailAddress)

    for user in groupUsers:
        print(user)
        if user['email'] == requestParam.userMailAddress:
            userRefID = user['refID']
    
    # ユーザのスケジュールをFirestoreに保存する
    insert_schedule(requestParam, userRefID)

    # 残りの入力状況を確認し、全員が入力できていればメールで通知する
    groupInfo = get_group_info_with_groupID_logic(groupID)
    if(len(groupInfo.schedules) == len(groupInfo.groupUsers)):
        print("投票完了")
        mailTitle = "全員の入力が完了しました。"
        mailBody = f"""
こちらから、みんなの投票状況を確認してください。
URL：https://sche-rem.vercel.app/check/{groupID}
        """
        send_emails(groupInfo.groupUsers[0], mailTitle, mailBody)

    return groupInfo