from django.db import models


class Social(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    link = models.URLField(max_length=150, null=True, blank=True)
