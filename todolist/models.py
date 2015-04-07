from django.db import models
from django.contrib.auth.models import User


class Common(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Board(Common):
    user = models.ForeignKey(User, related_name='boards')
    description = models.TextField(null=True)
    public = models.BooleanField(default=False)
    collabolators = models.ManyToManyField(User)


class List(Common):
    board = models.ForeignKey(Board, related_name='lists')


class Todo(Common):
    list = models.ForeignKey(List, related_name='todos')
    approved = models.BooleanField(default=False)