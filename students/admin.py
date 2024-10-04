from django.contrib import admin
from students.models import Student, Course, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'faculty', 'hobby')  # Fields to display in admin list view
    search_fields = ('first_name', 'last_name', 'email')  # Search by these fields
    list_filter = ('faculty', 'hobby')  # Filter by these fields

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'max_capacity', 'start_date', 'end_date')
    search_fields = ('course_name', 'course_code')
    list_filter = ('start_date', 'end_date')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'enrollment_date')
    list_filter = ('status', 'enrollment_date')
    search_fields = ('student__first_name', 'student__last_name', 'course__course_name')
