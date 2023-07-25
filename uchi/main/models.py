from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Mark(models.Model):
    mark = models.PositiveIntegerField("Оценка")
    def __str__(self):
        return f'{self.mark}'

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"


class Teachers(models.Model):
    name = models.CharField("Имя", max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"



class Subjects(models.Model):
    title = models.CharField("Название", max_length=50)
    idImage = models.ForeignKey(Image, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

class Courses(models.Model):
    title = models.CharField("Название", max_length=50)
    idMark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    idTeacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField("Длительность")
    idSubject = models.ForeignKey(Subjects, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lecture(models.Model):
    title = models.CharField("Название", max_length=50)
    info = models.TextField("Информация", max_length=5000)
    courses = models.ManyToManyField(Courses)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"


# class LectureCourses(models.Model):
#     idCourse = models.ForeignKey(Courses, on_delete=models.CASCADE)
#     idLecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
#     class Meta:
#         verbose_name = "Связь лекции и курсов"


class Lessons(models.Model):
    title = models.CharField("Название", max_length=50)
    info = models.TextField("Информация", max_length=5000)
    lectures = models.ManyToManyField(Lecture)
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title


# class LessonsLectures(models.Model):
#     idLecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
#     idLessons = models.ForeignKey(Lessons, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "Связь лекции и уроков"



