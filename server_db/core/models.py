from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class UserDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    value = models.TextField(default='', max_length=500)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return str(f'{self.id} - {self.user}')


class Student(models.Model):

    classs = (
        (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
        (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)
    )

    id = models.AutoField(primary_key=True, )
    name = models.CharField(max_length=100, default='')
    classX = models.CharField(choices=classs, default='0', max_length=2)
    school = models.CharField(max_length=100, default='')
    school_code = models.CharField(max_length=15, default='0')
    student_mobile = models.CharField(max_length=20, default='')

    father_name = models.CharField(max_length=100, default='')
    father_nid = models.CharField(max_length=17, default='0')
    father_mobile = models.CharField(max_length=20, default='')

    mother_name = models.CharField(max_length=100, default='')
    mother_nid = models.CharField(max_length=17, default='0')
    mother_mobile = models.CharField(max_length=20, default='')

    # present_address = models.TextField(max_length=500, default='')
    # permanent_address = models.TextField(max_length=500, default='')

    present_holding_code = models.CharField(max_length=10, default='')
    present_area = models.CharField(max_length=30, default='')
    present_district = models.CharField(max_length=20, default='')
    present_thana = models.CharField(max_length=20, default='')
    present_area_code = models.CharField(max_length=5, default='')    

    permanent_holding_code = models.CharField(max_length=10, default='')
    permanent_area = models.CharField(max_length=30, default='')
    permanent_district = models.CharField(max_length=20, default='')
    permanent_thana = models.CharField(max_length=20, default='')
    permanent_area_code = models.CharField(max_length=5, default='')


    def __str__(self):
        return self.name
