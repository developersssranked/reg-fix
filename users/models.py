from django.db import models
from django.contrib.auth.models import AbstractUser #импортируем уже созданный шаблон юзера

class User (AbstractUser):
    Image = models.ImageField(upload_to='user_images', null=True, blank= True) #на базе уже созданной модели мы добовляем свои нужные поля



