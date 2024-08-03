from django.db import models

# Create your models here.


class signup(models.Model):

    username = models.CharField(max_length=30)
    passward = models.CharField(max_length=30)

