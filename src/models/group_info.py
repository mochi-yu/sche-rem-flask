from models.schedule_info import ScheduleInfo

class GroupInfo:
    def __init__(self, groupID: str, groupName: str, author: str, groupUsers: list[str], schedules: list[ScheduleInfo], startDate: str, endDate: str, startHour: int, endHour: int ) -> None:
        self.groupID    = groupID
        self.schedule   = schedules
        self.groupName  = groupName
        self.author     = author
        self.groupUsers = groupUsers
        self.startDate  = startDate
        self.endDate    = endDate
        self.startHour  = startHour
        self.endHour    = endHour