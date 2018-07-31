from schedule import Schedule

s = Schedule("2018-05-20")
a = s.getDaySchedule(5)
lessons = a.get('lessons')
print(a.get('date'))
print(lessons[0].get('subject'))
print(s.getLessonType(lessons[0]))
print(s.getLessonTime(lessons[0]))
print(s.getLessonTeacherName(lessons[0]))
print(s.getGroupsNumbers(lessons[0]))
print(s.getLessonAddress(lessons[0]))