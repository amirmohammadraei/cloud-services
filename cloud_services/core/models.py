from django.db import models


class Comment(models.Model):
    username = models.CharField(max_length=20, null=False, blank=False)
    comment = models.CharField(max_length=1000, null=False, blank=False)
    photo = models.IntegerField(null=False, blank=False)
    is_toxic = models.BooleanField(default=False)


class Story(models.Model):
    username = models.CharField(max_length=20, null=False, blank=False)
    comment = models.CharField(max_length=1000, null=False, blank=False)
    photo = models.IntegerField(null=False, blank=False)