import requests
import json

class ScheduleParser:

    def __init__(self, url):
        self._url = url



    def getDaySchedule(self, day):
        """
        Getting schedule for a day
        :param day:
        :return dictrionary with the day schedule:
        """
        return list(json.loads(requests.get(self._url).text).values())[1][day].get('lessons')

    def getDayScheduleDate(self, day):
        """
        Getting date
        :param day:
        :return dictrionary with the date:
        """
        return list(self.decode().values())[1][day].get('date')

    def getLessonDescription(self, day, lesson):
        """
        Getting information about the lesson
        :param day , lesson:
        :return dictrionary with  the lesson description:
        """
        return self.getDaySchedule(day)[lesson]

    def getLessonName(self, day, lesson):
        """
        Getting name of the lesson
        :param day:
        :param lesson:
        :return: return the lesson name
        """
        return self.getLessonDescription(day, lesson).get('subject')

    def getLessonTime(self,day, lesson):
        """
        Getting time of the lesson
        :param day:
        :param lesson:
        :return: two strings with lesson start and end time
        """
        return self.getLessonDescription(day, lesson).get('time_start'), self.getLessonDescription(day, lesson).get('time_end')

    def getLessonType(self,day, lesson):
        """
        Getting type of the lesson
        :param day:
        :param lesson:
        :return: type of the lesson
        """
        return self.getLessonDescription(day, lesson).get('typeObj').get('name')

    def getGroupNumber(self, day, lesson):
        """
        Getting number of the the group
        :param day:
        :param lesson:
        :return: number of the group(str)
        """
        return self.getLessonDescription(day, lesson).get('groups')[0].get('name')

    def getLessonTeacherName(self, day, lesson):
        """
        Getting name of the lesson teacher
        :param day:
        :param lesson:
        :return: name of the teacher
        """
        return self.getLessonDescription(day, lesson).get('teachers')[0].get('full_name')

    def getLessonAddress(self, day, lesson):
        """
        Getting address of the lesson
        :param day:
        :param lesson:
        :return: address of the lesson
        """
        return self.getLessonDescription(day, lesson).get('auditories')[0].get('building').get('name') + ", ауд. " + self.getLessonDescription(day, lesson).get('auditories')[0].get('name')









url = "http://ruz2.spbstu.ru/api/v1/ruz/scheduler/24118?date=2018-5-14"
s = ScheduleParser(url)
a = s.getLessonAddress(0,0)
print(a)
