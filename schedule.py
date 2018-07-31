import requests
import json
from lesson import Lesson

class Schedule(Lesson):

    def __init__(self, date):
        self._url = "http://ruz2.spbstu.ru/api/v1/ruz/scheduler/24118?date=" + date

    def getWeekSchedule(self):
        """
        Getting week schedule
        :return: list with day's schedule
        """
        response = requests.get(self._url).text
        jsonData = json.loads(response)
        return jsonData['days']

    def getDaySchedule(self, day):
        """
        Getting day schedule
        :param day:
        :return: list with day information(weekday, date, lessons)
        """
        return self.getWeekSchedule()[day]



s = Schedule("2018-05-20")
a = s.getDaySchedule(5)
lessons = a.get('lessons')
print(a.get('date'))
print(lessons[1].get('subject'))
print(s.getLessonType(lessons[1]))
print(s.getLessonTime(lessons[1]))
print(s.getLessonTeacherName(lessons[2]))
print(s.getGroupsNumbers(lessons[1]))
print(s.getLessonAddress(lessons[1]))

