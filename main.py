from schedule import Schedule
from lesson import Lesson
import requests
import datetime


def main():
    s = Schedule()
    s.setDate("2018-04-18")

    for lesson in s.getDaySchedule(s._weekLentgh)['lessons']:
      esson = Lesson(lesson)
      print(lesson['subject'])
      print(esson.getLessonAddress())
      print(esson.getLessonTeacherName())

if __name__ == '__main__':
    main()