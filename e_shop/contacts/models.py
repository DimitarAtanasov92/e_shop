from django.db import models


class ContactUs(models.Model):
    title = models.CharField()
    message = models.TextField()
    email = models.EmailField()

