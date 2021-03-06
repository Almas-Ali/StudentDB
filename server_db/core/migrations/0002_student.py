# Generated by Django 3.1.6 on 2021-12-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('classX', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default='0', max_length=2)),
                ('school', models.CharField(default='', max_length=100)),
                ('school_code', models.CharField(default='0', max_length=15)),
                ('student_mobile', models.CharField(default='', max_length=20)),
                ('father_name', models.CharField(default='', max_length=100)),
                ('father_nid', models.CharField(default='0', max_length=17)),
                ('father_mobile', models.CharField(default='', max_length=20)),
                ('mother_name', models.CharField(default='', max_length=100)),
                ('mother_nid', models.CharField(default='0', max_length=17)),
                ('mother_mobile', models.CharField(default='', max_length=20)),
                ('present_holding_code', models.CharField(default='', max_length=10)),
                ('present_area', models.CharField(default='', max_length=30)),
                ('present_district', models.CharField(default='', max_length=20)),
                ('present_thana', models.CharField(default='', max_length=20)),
                ('present_area_code', models.CharField(default='', max_length=5)),
                ('permanent_holding_code', models.CharField(default='', max_length=10)),
                ('permanent_area', models.CharField(default='', max_length=30)),
                ('permanent_district', models.CharField(default='', max_length=20)),
                ('permanent_thana', models.CharField(default='', max_length=20)),
                ('permanent_area_code', models.CharField(default='', max_length=5)),
            ],
        ),
    ]
