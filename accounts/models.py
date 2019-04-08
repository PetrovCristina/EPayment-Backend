from django.db import models

# Create your models here.
from django.urls import reverse


class UploadedImage(models.Model):
    image = models.ImageField("Uploaded image",)  # stores the filename of an uploaded image


class User(models.Model):
    # the variable to take the inputs
    user_name = models.CharField(max_length=100, default='')
    user_surname = models.CharField(max_length=100, default='')
    user_phone = models.CharField(max_length=100, default='')
    user_email = models.EmailField(max_length=70, default='')
    user_pass = models.CharField(max_length=100, default='')
    face_encodings = models.BinaryField(null=True)


    # on submit click on the user entry page it redirects to the url below
    @staticmethod
    def get_absolute_url():
        return reverse('accounts:home')
