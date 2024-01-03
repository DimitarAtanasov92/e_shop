from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Profile(models.Model):
    email = models.EmailField(
        null=False, blank=False,
        unique=True
    )
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    img = models.ImageField(upload_to="user_img/", blank=True, null=True)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

