from django.db import models

class Blog(models.Model):
    post = models.CharField(max_length=200)
    date_post = models.DateField()
    discription = models.CharField(max_length=400)
