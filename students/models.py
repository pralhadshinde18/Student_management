from django.db import models
from django.core.validators import EmailValidator
from students.common.enum import Faculty,Hobby,Status


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    date_of_birth = models.DateField()
    faculty = models.CharField(max_length=50, choices=Faculty.choices(),default=Faculty.SCIENCE.value)
    hobby = models.CharField(max_length=50, choices=Hobby.choices(),default=Hobby.CRICKET.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    max_capacity = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['course_code']

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"

    def is_full(self):
        return self.enrollment_set.count() >= self.max_capacity

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices(), default=Status.ENROLLED)
    enrollment_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['student', 'course']]
        ordering = ['-enrollment_date']

    def __str__(self):
        return f"{self.student} - {self.course} ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        if not self.pk and self.course.is_full():
            raise ValueError("Course has reached maximum capacity")
        super().save(*args, **kwargs)


