class Lesson:

    def __init__(self, lesson):
        self._lesson = lesson

    def getLessonTime(self):
        """
        Getting time of the lesson
        :return: two strings with lesson start and end time
        """
        return self._lesson['time_start'], self._lesson['time_end']

    def getLessonType(self):
        """
        Getting type of the lesson
        :return: type of the lesson
        """
        return self._lesson['typeObj']['name']

    def getGroupsNumbers(self):
        """
        Getting number of the the group
        :return: number of the group(str)
        """
        groups = [group['name'] for group in self._lesson['groups']]
        return ', '.join(groups)

    def getLessonTeacherName(self):
        """
        Getting name of the lesson teacher
        :return: name of the teacher
        """
        try:
          teacherName = self._lesson['teachers'][0]['full_name']
        except:
          teacherName = "Неизвестно"

        return teacherName

    def getLessonAddress(self):
        """
        Getting address of the lesson
        :return: address of the lesson
        """
        try:
          Address = self._lesson['auditories'][0]['building']['name'] + ", ауд. " + self._lesson['auditories'][0]['name']
        except:
          Address = "Неизвестно"

        return Address
