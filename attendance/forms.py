# students/forms.py
from django import forms
from .models import Student, Lecturer, Course, Admin, Attendance


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birthdate', 'phone', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Hide the password input
            'birthdate': forms.DateInput(attrs={'type': 'date'}),  # Use a date picker for birthdate
        }


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['first_name', 'last_name', 'birthdate', 'phone', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Hide the password input
            'birthdate': forms.DateInput(attrs={'type': 'date'}),  # Use a date picker for birthdate
        }


class CourseForm(forms.ModelForm):
    lecturer = forms.ModelChoiceField(queryset=Lecturer.objects.all(), empty_label="Select Lecturer")

    class Meta:
        model = Course
        fields = ['course_code', 'name', 'hours', 'lecturer']


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'phone', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Hide the password input
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'course', 'lecturer', 'status', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Use a date picker for date
        }

    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)
