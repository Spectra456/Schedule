from schedule import Schedule
from lesson import Lesson


def main():
    s = Schedule()
    s.setDate("2018-05-20")
    a = s.getDaySchedule(5)
    lessons = a['lessons']


    for lesson in s.getDaySchedule(5)['lessons']:
      esson = Lesson(lesson)
      print(lesson['subject'])
      print(esson.getLessonType())
      print(esson.getGroupsNumbers())

if __name__ == '__main__':
    main()