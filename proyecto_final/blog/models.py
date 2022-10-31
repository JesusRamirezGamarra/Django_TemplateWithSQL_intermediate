from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
# from django.utils import timezone
# from datetime import datetime


# Create your models here.
User = get_user_model()
class Author(models.Model):
    """Author utilizando el listado de Users del sistema"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        # print(self.user)
        # breakpoint()
        return f"""{self.user.first_name} {self.user.last_name} """


class Category(models.Model):
    """Category que agrupa Post"""

    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """Post"""

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()   
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title


class Donation_Goal(models.Model):
    """Objetivo monto total de la donacion con parametros de vigencia"""

    class Meta:
        verbose_name_plural = "Donations Goal"

    goal = models.IntegerField()
    description = models.CharField(max_length=500)
    startdate = models.DateField()
    enddate = models.DateField()
    active = models.BooleanField()
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        activo =  "Activo" if self.active else "Inactivo"
        return "%s : [    Inicio: %s  - Fin:  %s  ] %s " % (
            activo,
            self.startdate,
            self.enddate,
            self.description,
        )


class JobGroup(models.Model):
    """Monto : JobGroup para Jobs listado  """

    name = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        job = Job.objects.filter(jobgroup=f"{self.id}")
        return "[    %s  Jobs ]: %s" % (
            len(job), 
            self.name
        )
        # return self.jobgroup


class Job(models.Model):
    """Monto : Jobs listado  """

    name = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    jobgroup = models.ForeignKey(JobGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "[   ID-%s  ]-[    %s  ]: %s" % (
            self.id,
            self.jobgroup.name, 
            self.name
        )
        # return self.job

class Donation(models.Model):
    """Info : del Donante"""

    firtsname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    # job = models.CharField(max_length=40)

    createdate = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation_Goal = models.ForeignKey(Donation_Goal, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s  : [ %s ]" % (
            self.firtsname,
            self.firtsname, 
            self.email
        )
    
class Collaboration(models.Model):
    """Monto : donado """

    amount  = models.IntegerField()
    # job = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.amount, self.createdate)
    
    
class Embrace(models.Model):
    """Formulario Solitud de Adopcion"""
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()
    # description =RichTextField()
    
    
class Contact(models.Model):
    """Formulario de Conactanos"""
    
    name = models.CharField(max_length=50)    
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    # message = RichTextField()
    

class Suscripcion(models.Model):
    name = models.CharField(max_length=50)    
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class  Meta:   #new
        verbose_name_plural  =  "User Colaborator Suscripcions"                    
    
class Perfil(models.Model):
    name = models.CharField(max_length=50)    
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class  Meta:   #new
        verbose_name_plural  =  "User Colaborator Perfils"               
        
        
from django.contrib.auth.models import User 

class UserColaborator(models.Model):
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=70)
    pwd = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to ='avatar',max_length=None, blank=True,null=True)
    perfil= models.ForeignKey(Perfil, on_delete=models.CASCADE)
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    # user = models.Foreignkey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class  Meta:   #new
        verbose_name_plural  =  "User colaborators"        

class PostUserColaborator(models.Model):
    user = models.ForeignKey(UserColaborator, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True,null=True)#
    createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    class  Meta:   #new
        verbose_name_plural  =  "User Post colaborators"    