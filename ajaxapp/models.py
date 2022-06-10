from django.db import models

# Create your models here.
class Friend(models.Model):
    nick_name=models.CharField(max_length=100, unique=True)
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    likes = models.CharField(max_length = 250)
    # auto_now -updates value of field to current time & date every time the Model.save() is called/ everytime obj is saved
    # auto_now_add -updates the value with the time and date of creation of record initially in the database.
    dob = models.DateField(auto_now=False,auto_now_add=False)
    lives_in = models.CharField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.nick_name
