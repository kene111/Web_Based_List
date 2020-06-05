from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    Item = models.CharField(max_length=500)
    Date_Posted = models.DateTimeField(default=timezone.now)
    Specification = models.TextField(default='')
    Created_By = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Created_By')
    Price = models.IntegerField()
    Modified_Date = models.DateTimeField(null = True)
    Modified_By = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='Modified_By')
 
    def __str__(self):
        return self.Item 

    def get_absolute_url(self):
    	return reverse('post-detail', kwargs = {'pk': self.pk })



   

        




