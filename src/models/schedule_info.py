class ScheduleInfo:
    def __init__(self, scheduleInfo) -> None:
        self.userMailAdress = scheduleInfo["userMailAddress"]

        newScheduleArray = []
        for i in range(len(scheduleInfo["scheduleInfo"])):
            newScheduleArray.append(scheduleInfo["scheduleInfo"][str(i)])

        self.scheduleInfo = newScheduleArray