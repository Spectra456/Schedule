class Lesson:

    def getLessonTime(self,lesson):
        """
        Getting time of the lesson
        :param lesson:
        :return: two strings with lesson start and end time
        """
        return lesson['time_start'], lesson['time_end']

    def getLessonType(self, lesson):
        """
        Getting type of the lesson
        :param lesson:
        :return: type of the lesson
        """
        return lesson['typeObj']['name']

    def getGroupsNumbers(self, lesson):
        """
        Getting number of the the group
        :param lesson:
        :return: number of the group(str)
        """
        groups = [group['name'] for group in lesson['groups']]
        return ', '.join(groups)

    def getLessonTeacherName(self, lesson):
        """
        Getting name of the lesson teacher
        :param lesson:
        :return: name of the teacher
        """
        try:
          teacherName = lesson['teachers'][0]['full_name']
        except:
          teacherName = "Неизвестно"

        return teacherName

    def getLessonAddress(self,lesson):
        """
        Getting address of the lesson
        :param lesson:
        :return: address of the lesson
        """
        try:
          Address = lesson['auditories'][0]['building']['name'] + ", ауд. " + lesson['auditories'][0]['name']
        except:
          Address = "Неизвестно"

        return Address

        return lesson['auditories'][0]['building']['name'] + ", ауд. " + lesson['auditories'][0]['name']