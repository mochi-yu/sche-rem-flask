class SubmitGroupRequestParam:
    def __init__(self, userName: str, userMailAddress: str, scheduleInfo: list[list[bool]]) -> None:
        self.userName         = userName
        self.userMailAddress  = userMailAddress
        self.scheduleInfo     = scheduleInfo
