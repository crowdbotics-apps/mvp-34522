from django.conf import settings
from django.db import models


class Course(models.Model):
    "Generated Model"
    name = models.TextField()
    units = models.IntegerField(
        null=True,
        blank=True,
    )


# Create your models here.
