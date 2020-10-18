from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    avatar = models.ImageField(upload_to="avatars", blank=True)
    favs = models.ManyToManyField("api.FoodDatas", related_name="favs")