from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"""{self.name}"""    
    
class Message(models.Model):
    # id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
    def __str__(self):
        return f"""{self.room} {self.user}"""        
