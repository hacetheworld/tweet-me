from django.db import models

# Create your models here.


class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(
        upload_to="images/", max_length=100, blank=True, null=True)
