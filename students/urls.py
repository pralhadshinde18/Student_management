from django.urls import path

# from students.views import create_student
# from students.views import get_students
# from students.views import get_student
# urlpatterns = [
#     path('student/create', create_student, name='create_student'),
#     path('students/', get_student, name='get_students')
#
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet, CourseViewSet, EnrollmentViewSet


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]