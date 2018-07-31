import requests
import json

class ScheduleParser:

    def __init__(self, url):
        self.__url = url

    def request(self):
        return requests.get(self.__url)

    def decode(self):
        """
        Decoding JSON from our request
        :return dictrionary with week schedule:
        """
        return json.loads(self.request().text)

    def getDaySchedule(self, day):
        """
        Getting schedule for a day
        :param day:
        :return dictrionary with day schedule:
        """
        return list(self.decode().values())[1][day].get('lessons')

    def getDayScheduleDate(self, day):
        """
        Getting date
        :param day:
        :return dictrionary with date:
        """
        return list(self.decode().values())[1][day].get('date')

    def getLessonDescription(self, day, lesson):
        """
        Getting information about lesson
        :param day , lesson:
        :return dictrioary with lesson description:
        """
        return self.getDaySchedule(day)[lesson]

    def getLessonName(self, day, lesson):
        """
        Getting name of lesson
        :param day:
        :param lesson:
        :return:
        """
        return self.getLessonDescription(day, lesson)







url = "http://ruz2.spbstu.ru/api/v1/ruz/scheduler/24118?date=2018-5-14"
s = ScheduleParser(url)
print(s.getDayScheduleDate(0))