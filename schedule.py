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



