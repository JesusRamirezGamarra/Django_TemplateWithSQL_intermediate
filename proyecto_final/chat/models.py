from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    """Room : Room unico que agrupa mensajes para el CHAT"""    
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)       
    def __str__(self):
        return f"""{self.name}"""    
    class  Meta:
        verbose_name = " User:Room"
        verbose_name_plural  =  "Room [ User:Room ]"    
        
    
class Message(models.Model):
    """Message : Message por Usuario agrupados por Room"""        
    value = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)       
    def __str__(self):
        return f"""{self.room} {self.user}"""
    class  Meta:
        verbose_name = " Mensaje"
        verbose_name_plural  =  "Message [ Mensaje ]"        
