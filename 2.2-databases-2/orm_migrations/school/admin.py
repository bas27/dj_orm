from django.contrib import admin

from .models import Student, Teacher

class StudentInline(admin.TabularInline):
    model = Student.teacher.through
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['group']
    inlines = [
        StudentInline,
    ]
    exclude = ('teacher',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['subject']
    inlines = [
        StudentInline,
    ]
