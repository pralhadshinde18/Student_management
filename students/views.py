from students.models import Student, Course, Enrollment
from students.serializers import StudentSerializer
from students.serializers import CourseSerializer
from students.serializers import EnrollmentSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters


class StudentFilter(filters.FilterSet):
    min_age = filters.NumberFilter(field_name="date_of_birth", lookup_expr='year__lte')
    max_age = filters.NumberFilter(field_name="date_of_birth", lookup_expr='year__gte')
    faculty = filters.CharFilter(lookup_expr='iexact')
    hobby = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Student
        fields = ['faculty', 'hobby', 'min_age', 'max_age']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = StudentFilter
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name', 'date_of_birth']

    @action(detail=True, methods=['get'])
    def enrollments(self, request, pk=None):
        student = self.get_object()
        enrollments = student.enrollment_set.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['course_name', 'course_code']
    ordering_fields = ['course_name', 'start_date', 'end_date']

    @action(detail=True, methods=['get'])
    def enrolled_students(self, request, pk=None):
        course = self.get_object()
        enrollments = course.enrollment_set.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status']
    ordering_fields = ['enrollment_date', 'status']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
