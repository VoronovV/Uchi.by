from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('entrace', views.entrace),
    path('registration', views.registration),
    path('logout', views.logout, name='logout'),
    path('exit', views.exit),
    path('full_course/<int:course_id>/', views.full_course, name='full_course'),
    path('<int:course_id>/', views.courseDetail, name='courseDetail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
