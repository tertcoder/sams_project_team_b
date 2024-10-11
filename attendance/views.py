# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, LecturerForm, CourseForm, AdminForm, AttendanceForm
from .models import Student, Lecturer, Course, Admin, Attendance
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Student Views
def student_form(request):
    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_student_url')  # Ensure this matches the name in urls.py
    return render(request, 'student_form.html', {'form': form})


def success_view(request):
    students = Student.objects.all()  # Get all students
    return render(request, 'success.html', {'students': students})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('success_student_url')
    return render(request, 'confirm_delete.html', {'object': student})


def modify_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_student_url')
    return render(request, 'modify_student.html', {'form': form})


# Lecturer Views
def lecturer_form(request):
    form = LecturerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_lecturer_url')
    return render(request, 'lecturer_form.html', {'form': form})


def success_lecturer_view(request):
    lecturers = Lecturer.objects.all()  # Get all lecturers
    return render(request, 'success_lecturer.html', {'lecturers': lecturers})


def delete_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    if request.method == 'POST':
        lecturer.delete()
        return redirect('success_lecturer_url')
    return render(request, 'confirm_delete.html', {'object': lecturer})


def modify_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    form = LecturerForm(request.POST or None, instance=lecturer)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_lecturer_url')
    return render(request, 'modify_lecturer.html', {'form': form})


# Course Views
def course_form(request):
    form = CourseForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_course_url')
    lecturers = Lecturer.objects.all()  # Get all lecturers
    return render(request, 'course_form.html', {'form': form, 'lecturers': lecturers})


def success_course_view(request):
    courses = Course.objects.all()  # Get all courses
    return render(request, 'success_course.html', {'courses': courses})


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('success_course_url')
    return render(request, 'confirm_delete.html', {'object': course})


def modify_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, instance=course)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_course_url')
    return render(request, 'modify_course.html', {'form': form})


# Admin Views
def admin_form_view(request):
    form = AdminForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_admin')
    return render(request, 'students/admin_form.html', {'form': form})


def success_admin_view(request):
    admins = Admin.objects.all()
    return render(request, 'students/success_admin.html', {'admins': admins})


def modify_admin_view(request, id):
    admin = get_object_or_404(Admin, id=id)
    form = AdminForm(request.POST or None, instance=admin)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('success_admin')
    return render(request, 'modify_admin.html', {'form': form})


def delete_admin_view(request, id):
    admin = get_object_or_404(Admin, id=id)
    if request.method == 'POST':
        admin.delete()
        return redirect('success_admin')
    return render(request, 'confirm_delete.html', {'object': admin})


# Attendance Views
def attendance_list(request):
    attendances = Attendance.objects.all()  # Retrieve all attendance records
    return render(request, 'Attendance_list.html', {'attendances': attendances})


def add_attendance(request):
    form = AttendanceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('attendance_list')
    return render(request, 'add_attendance.html', {'form': form})


def modify_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    form = AttendanceForm(request.POST or None, instance=attendance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('attendance_list')
    return render(request, 'modify_attendance.html', {'form': form})


def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    if request.method == "POST":
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'confirm_delete.html', {'object': attendance})


def attendance_per_student(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    attendance_records = Attendance.objects.all()

    if request.method == "POST":
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course')
        date = request.POST.get('date')

        # Filter by student name or ID
        filters = Q()
        if student_name:
            filters |= Q(student__first_name__icontains=student_name)  # Adjust 'first_name' if needed
        if student_id:
            filters |= Q(student__id=student_id)

        attendance_records = attendance_records.filter(filters)

        # Filter by course
        if course_id:
            attendance_records = attendance_records.filter(course_id=course_id)

        # Filter by date
        if date:
            attendance_records = attendance_records.filter(date=date)

    return render(request, 'attendance_per_student.html', {
        'students': students,
        'courses': courses,
        'attendance_records': attendance_records,
    })


# Authentication Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    return render(request, 'home.html')  # Change to your home page template
