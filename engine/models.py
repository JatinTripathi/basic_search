from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.TextField(null = True)

class Image(models.Model):
    url = models.TextField(null = True)

class TagImageScore(models.Model):
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE, null = True)
    image = models.ForeignKey(Image, on_delete = models.CASCADE, null = True)
    score = models.IntegerField(default = 0, null = True)