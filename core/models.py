from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"Contacted By - {self.name}"


class SocialMedia(models.Model):
    facebook = models.CharField(max_length=50)
    insta = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    email = models.CharField(max_length=50)