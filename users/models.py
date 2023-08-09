from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager
from users.validators import validate_file_extension


# Create your models here.

def get_file_path(instance, filename):
    return f'user_documents/{instance.user.email}/{filename}'


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = UserManager()

    def __str__(self):
        return self.email


class UserUploadedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    uploaded_date = models.DateField(auto_now=True)
    file = models.FileField(upload_to=get_file_path, validators=[validate_file_extension])
