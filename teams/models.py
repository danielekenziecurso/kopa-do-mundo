from datetime import datetime
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(default=0, null=True, blank=True)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(null=True, blank=True)


def __str__(self):
    return f"{self.name} - {self.fifa_code}"
