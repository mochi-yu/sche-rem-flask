import requests

from models.schedule_info import ScheduleInfo

sampleData = [
    {
        "userMailAddress": "aaaaa",
        "scheduleInfo": [
            [True, True],
            [True, True],
        ]
    },
    {
        "userMailAddress": "aaaaa",
        "scheduleInfo": [
            [True, True],
            [True, True],
        ]
    }
]

def get_schedules(groupUserRefIDs: list[int]):
    response = requests.post(
        "https://us-central1-sche-rem.cloudfunctions.net/getSchedule",
        data={'refIDs': groupUserRefIDs}
    )

    return response.json()

def insert_schedule(scheduleInfo: ScheduleInfo, groupUserRefID: int):
    print({
        'refID': groupUserRefID,
        'schedule': scheduleInfo.__dict__
    })
    response = requests.post(
        "https://us-central1-sche-rem.cloudfunctions.net/postSchedule",
        json={
            "refID": str(groupUserRefID),
            "schedule": scheduleInfo.__dict__
        },
    )

    return scheduleInfo