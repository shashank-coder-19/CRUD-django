from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=264)
    principal=models.CharField(max_length=264)
    location=models.CharField(max_length=264)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail',kwargs={'pk':self.pk})

        # it is telling django to go back to detail page of that particualar pk if no other url is provided


class Student(models.Model):
    name=models.CharField(max_length=264)
    age=models.PositiveIntegerField()
    school=models.ForeignKey('School',related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
