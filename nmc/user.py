class User:
    def __init__(self, id, passwd, mob):
        self.id = id
        self.passwd = passwd
        self.mob = mob


# class Schedule:
#     def __init__(self, hr, mn):
#         self.hr = hr
#         self.mn = mn


class UserSchedule:
    def __init__(self, id, schedule_list):
        self.schedule_list = schedule_list
