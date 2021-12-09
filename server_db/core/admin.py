from tkinter.constants import S
from django.contrib import admin
from core.models import (
    UserDetail,
    Student
)

admin.site.register(UserDetail)
admin.site.register(Student)
