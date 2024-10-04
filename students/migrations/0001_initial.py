# Generated by Django 5.1.1 on 2024-10-04 11:17

import django.core.validators
import django.db.models.deletion
import students.common.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['course_code'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('date_of_birth', models.DateField()),
                ('faculty', models.CharField(choices=[('science', 'SCIENCE'), ('commerce', 'COMMERCE'), ('art', 'ART')], default='science', max_length=50)),
                ('hobby', models.CharField(choices=[('cricket', 'CRICKET'), ('tennis', 'TENNIS')], default='cricket', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Enrolled', 'ENROLLED'), ('Completed', 'COMPLETED'), ('Dropped', 'DROPPED'), ('Withdrawn', 'WITHDRAWN')], default=students.common.enum.Status['ENROLLED'], max_length=20)),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
            options={
                'ordering': ['-enrollment_date'],
                'unique_together': {('student', 'course')},
            },
        ),
    ]