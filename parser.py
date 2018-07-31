import requests
import json

class ScheduleParser:

    def __init__(self, url):
        self._url = url

    def getWeekSchedule(self):
        """
        Getting week schedule
        :return: list with day's schedule
        """
        return list(json.loads(requests.get(self._url).text).values())[1]

    def getDaySchedule(self, day):
        """
        Getting day schedule
        :param day:
        :return: list with day information(weekday, date, lessons)
        """
        return self.getWeekSchedule()[day]


    def getLessonTime(self,lesson):
        """
        Getting time of the lesson
        :param day:
        :param lesson:
        :return: two strings with lesson start and end time
        """
        return lesson.get('time_start'), lesson.get('time_end')

    def getLessonType(self, lesson):
        """
        Getting type of the lesson
        :param day:
        :param lesson:
        :return: type of the lesson
        """
        return lesson.get('typeObj').get('name')

    def getGroupsNumbers(self, lesson):
        """
        Getting number of the the group
        :param day:
        :param lesson:
        :return: number of the group(str)
        """
        groups = ""
        for group in range(len(lesson.get('groups'))):
            groups = groups + " ," + lesson.get('groups')[group].get('name')
        return groups

    def getLessonTeacherName(self, lesson):
        """
        Getting name of the lesson teacher
        :param day:
        :param lesson:
        :return: name of the teacher
        """
        return lesson.get('teachers')[0].get('full_name')

    def getLessonAddress(self,lesson):
        """
        Getting address of the lesson
        :param day:
        :param lesson:
        :return: address of the lesson
        """
        return lesson.get('auditories')[0].get('building').get('name') + ", ауд. " + lesson.get('auditories')[0].get('name')









url = "http://ruz2.spbstu.ru/api/v1/ruz/scheduler/24118?date=2018-5-14"
s = ScheduleParser(url)
a = s.getDaySchedule(5)
lessons = a.get('lessons')
a = s.getLessonAddress(lessons[0])
print(a)
#  Получение лессонов
