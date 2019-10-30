from django.contrib import admin
from .models import Student, Semester, Section, Instructor, Registration, Course, Period, Year

admin.site.register(Year)
admin.site.register(Period)
admin.site.register(Semester)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Registration)
admin.site.register(Course)
# Register your models here.
