from django.db import models


class Organization(models.Model):
    login = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    score = models.IntegerField()

    def __str__ (self):
        return self.login
