import requests
import json
import datetime


class Schedule():

    def __init__(self):
        self._url = "http://ruz2.spbstu.ru/api/v1/ruz/scheduler/24118"

        today = datetime.datetime.today()
        a = today.strftime("%Y-%m-%d")
        self._date = {'date': a}

        self._weekLentgh = 0

    def setDate(self, date):

        self._date = {'date': date}

    def getWeekSchedule(self):
        """
        Getting week schedule
        :return: list with day's schedule
        and changing weekLentgh
        """

        response = requests.get(self._url, params= self._date).text
        jsonData = json.loads(response)

        self._weekLentgh = len(jsonData['days'])
        return jsonData['days']

    def getDaySchedule(self, day):
        """
        Getting day schedule
        :param day:
        :return: list with day information(weekday, date, lessons)
        """
        return self.getWeekSchedule()[day]



