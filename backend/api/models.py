from django.db import models
from django.contrib.auth.models import User # we don't need to make a User , we already have User built in bro
# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)#auto_now_add gives the date and time of creation of this data
    author = models.ForeignKey(User,on_delete=models.CASCADE , related_name="notes")
    #related name is useful when i know the user and I need to get the user's notes
    #I can just type user.notes.all() .

    def __str__(self):
        return self.title

