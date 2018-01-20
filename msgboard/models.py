from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=1024)

class Topic(models.Model):
    name = models.CharField(max_length=32)
    userId = models.ForeignKey(User)
    dateCreated = models.DateTimeField(default=now, null=True)
    isLocked = models.BooleanField(default=False)
    boardId = models.ForeignKey(Board, on_delete=models.CASCADE)

class Msg(models.Model):
    userId = models.ForeignKey(User)
    text = models.CharField(max_length=2048)
    likes = models.IntegerField(default=0)
    dateCreated = models.DateTimeField(default=now, null=True)
    TopicId = models.ForeignKey(Topic, on_delete=models.CASCADE)