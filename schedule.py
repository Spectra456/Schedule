import requests
import json

class Schedule:

    def __init__(self, url):
        self._url = url

    def getWeekSchedule(self):
        """
        Getting week schedule
        :return: list with day's schedule
        """
        jsonData = json.loads(requests.get(self._url).text)
        return list(jsonData.values())[1]

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
        :param lesson:
        :return: two strings with lesson start and end time
        """
        return lesson.get('time_start'), lesson.get('time_end')

    def getLessonType(self, lesson):
        """
        Getting type of the lesson
        :param lesson:
        :return: type of the lesson
        """
        return lesson.get('typeObj').get('name')

    def getGroupsNumbers(self, lesson):
        """
        Getting number of the the group
        :param lesson:
        :return: number of the group(str)
        """
        groupsNum = len(lesson.get('groups'))
        groups = [None] * groupsNum
        for group in range(groupsNum):
            groups[group] = lesson.get('groups')[group].get('name')
        return groups

    def getLessonTeacherName(self, lesson):
        """
        Getting name of the lesson teacher
        :param lesson:
        :return: name of the teacher
        """
        return lesson.get('teachers')[0].get('full_name')

    def getLessonAddress(self,lesson):
        """
        Getting address of the lesson
        :param lesson:
        :return: address of the lesson
        """
        return lesson.get('auditories')[0].get('building').get('name') + ", ауд. " + lesson.get('auditories')[0].get('name')



url = "http://ruz2.spbstu.ru/api/v1/ruz/scheduler/24118?date=2018-5-14"
s = Schedule(url)
a = s.getDaySchedule(5)
lessons = a.get('lessons')
print(a.get('date'))
print(lessons[0].get('subject'))
print(s.getLessonType(lessons[0]))
print(s.getLessonTime(lessons[0]))
print(s.getLessonTeacherName(lessons[0]))
print(s.getLessonAddress(lessons[0]))

