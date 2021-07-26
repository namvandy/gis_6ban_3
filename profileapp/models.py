from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model): # target_user.profile <- profile로 접근하는 방법
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile') # cascade: 종속
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)



