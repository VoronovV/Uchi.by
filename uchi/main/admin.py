from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Courses)
admin.site.register(Lecture)
# admin.site.register(LectureCourses)
admin.site.register(Lessons)
admin.site.register(Teachers)
# admin.site.register(LessonsLectures)
admin.site.register(Subjects)
admin.site.register(Mark)
admin.site.register(Image)
