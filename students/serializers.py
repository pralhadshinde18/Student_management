from rest_framework import serializers
from students.models import Student
from students.models import Course
from students.models import Enrollment

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
#         # fields = ['id', 'first_name','last_name','date_of_birth','field','hobby']
#
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'
#
# class EnrollmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Enrollment
#         fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_date_of_birth(self, value):
        from django.utils.timezone import now
        if value > now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future")
        return value

class CourseSerializer(serializers.ModelSerializer):
    current_capacity = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_current_capacity(self, obj):
        return obj.enrollment_set.count()

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    course_name = serializers.CharField(source='course.course_name', read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'

    def validate(self, data):
        course = data['course']
        if not self.instance:
            if course.is_full():
                raise serializers.ValidationError(
                    f"Course {course.course_code} has reached its maximum capacity"
                )
        return data
