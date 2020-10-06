from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Students(models.Model):
    name= models.CharField(max_length=100)
    mobile=models.IntegerField()
    email= models.CharField(max_length=100)
    image= models.ImageField(upload_to='images')
    offer=models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf =  models.FileField(upload_to='pdf')
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete
        super().delete(*args, **kwargs)  # Call the "real" save() method.


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
## practice many to many relationship with models
class Movie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
         return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
         return self.name

##############################################################
class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    age= models.IntegerField()

    def __str__(self):
        return self.user.username
