from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.


def index(request):
    courses = Courses.objects.all()
    img = Image.objects.all()
    subject = Subjects.objects.all()
    auth = settings.MY_GLOBAL_VAR
    context = {
        'auth': auth,
        'courses': courses,
        'img': img,
        'subject': subject
    }
    return render(request, 'main/index.html', context)


def entrace(request):
    auth = settings.MY_GLOBAL_VAR

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username, password=password)
        if user:
            settings.MY_GLOBAL_VAR = {'auth': 1}
            auth = settings.MY_GLOBAL_VAR
            return redirect('/', auth=auth)
        else:
            return redirect('/entrace')
        # return render(request, 'main/index.html', auth)

    return render(request, 'main/entrace.html', auth)


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatPassword')

        user = User.objects.filter(username=username, password=password)

        if not user:
            if password != repeatPassword:
                return redirect('/registration')
            else:
                user = User(username=username, password=password)
                user.save()
                settings.MY_GLOBAL_VAR = {'auth': 1}
                auth = settings.MY_GLOBAL_VAR
                return redirect('/', auth=auth)
        else:
            return redirect('/registration')

    return render(request, 'main/registration.html')


def exit(request):
    return render(request, 'main/exit.html', {'auth' : 1})


def logout(request):
    settings.MY_GLOBAL_VAR = {'auth': 2}
    auth = settings.MY_GLOBAL_VAR
    return redirect('/', auth=auth)
    # return render(request, 'main/index.html', auth)


def courseDetail(request, course_id):
    course = Courses.objects.get(id=course_id)

    lectures = Lecture.objects.filter(courses__id=course_id)
    # lecturesInfo = Lecture.objects.filter(id=lectures.idLecture)

    # lessons = LessonsLectures.objects.filter(lectures__id=lectures.id)
    # # lessonsInfo = Lessons.objects.filter(id=lessons.idLessons)
    #
    # subject = Subjects.objects.filter(id=course.idSubject)
    # img = Image.objects.filter(id=subject.idImage)
    context = { 'course': course,
                'auth':  settings.MY_GLOBAL_VAR,
                'lectures': lectures,
                }
    return render(request, 'main/courseDetail.html', context)

def full_course(request, course_id):
    if settings.MY_GLOBAL_VAR == {'auth': 2}:
        # доделать с ошибкой
        return redirect('/entrace')
    course = Courses.objects.get(id=course_id)

    lectures = Lecture.objects.filter(courses__id=course_id)
    context = {'course': course,
               'auth': settings.MY_GLOBAL_VAR,
               'lectures': lectures,
               }
    return render(request, 'main/full_course.html', context)