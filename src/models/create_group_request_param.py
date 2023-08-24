class CreateGroupRequestParam:
    def __init__(self, groupName: str, author: str, groupUsers: list[str], startDate: str, endDate: str, startHour: int, endHour: int ) -> None:
        self.groupName  = groupName
        self.author     = author
        self.groupUsers = groupUsers
        self.startDate  = startDate
        self.endDate    = endDate
        self.startHour  = startHour
        self.endHour    = endHour