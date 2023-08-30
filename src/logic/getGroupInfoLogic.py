from database.GroupInformationTable import get_group
from database.GroupUserTable import get_users
from database.ScheduleInfoTable import get_schedules
from models.schedule_info import ScheduleInfo
from models.group_info import GroupInfo

def get_group_info_with_groupID_logic(groupID):
    groupInfo = get_group(groupID)

    groupUsers = get_users(groupID)
    groupUserEmails = []
    groupUserRefIDs = []
    for user in groupUsers:
        groupUserRefIDs.append(user["refID"])
        groupUserEmails.append(user["email"])

    scheduleInfo = get_schedules(groupUserRefIDs)
    scheduleInfos: list[ScheduleInfo] = []
    for sche in scheduleInfo:
        scheduleInfos.append(ScheduleInfo(sche))

    groupInfo["groupUsers"] = groupUserEmails
    groupInfo["schedules"] = scheduleInfos

    return GroupInfo(**groupInfo)