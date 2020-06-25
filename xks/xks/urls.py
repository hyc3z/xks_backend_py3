from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
import student.views
import teacher.views
import sysadmin.views

studentRouter = routers.DefaultRouter()
studentRouter.register(r'students', student.views.StudentViewSet)
studentRouter.register(r'choosecourses', student.views.ChooseCourseViewSet)

sysadminRouter = routers.DefaultRouter()
sysadminRouter.register(r'systemadmins', sysadmin.views.SystemAdminViewSet)
sysadminRouter.register(r'terms', sysadmin.views.TermViewSet)

teacherRouter = routers.DefaultRouter()
teacherRouter.register(r'teachers', teacher.views.TeacherViewSet)
teacherRouter.register(r'offercourses', teacher.views.OfferCourseViewSet)

base_urlpatterns= [
    url(r'^student/', include(studentRouter.urls)),
    url(r'^student/get_offer_courses/$', student.views.GetOfferCourses.as_view(), name='get-offer-courses'),
    url(r'^student/get_chosen_courses/$', student.views.GetChosenCourses.as_view(), name='get-chosen-courses'),
    url(r'^student/get_course_score/$', student.views.GetCourseScore.as_view(), name='get-course-score'),

    url(r'^sysadmin/', include(sysadminRouter.urls)),
    url(r'^teacher/', include(teacherRouter.urls)),
]

urlpatterns = [
    url(r'^api/', include(base_urlpatterns)),
    path('admin/', admin.site.urls),
]
