from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class UserDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    value = models.TextField(default='', max_length=500)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return self.sno
