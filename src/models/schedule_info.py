class ScheduleInfo:
    def __init__(self, userMailAddress: str, scheduleInfo: list[list[bool]]) -> None:
        self.userMailAdress = userMailAddress
        self.scheduleInfo = scheduleInfo