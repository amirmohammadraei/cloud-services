from django.db import models


class Comment(models.Model):
    username = models.CharField(max_length=20, null=False, blank=False)
    comment = models.CharField(max_length=1000, null=False, blank=False)
    photo = models.IntegerField(null=False, blank=False)
    is_toxic = models.BooleanField(default=False)
    music = models.FileField(upload_to='media', null=True)

    def __str__(self):
        return f'{self.username}'


class Story(models.Model):
    username = models.CharField(max_length=20, null=False, blank=False)
    story = models.TextField(null=False, blank=False)
    photo = models.IntegerField(null=False, blank=False)
    music = models.FileField(upload_to='music', null=True)

    def __str__(self):
        return f'{self.username}'
