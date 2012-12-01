from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=300)
