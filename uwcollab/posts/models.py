from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    """
    Represents a location where electricity usage is being recorded.
    """
    name = models.ForeignKey('User')
    title = models.CharField(max_length=20)
    content = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    program = models.CharField(max_length=30)
