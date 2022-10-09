from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime


# Create your models here.
User = get_user_model()


class Author(models.Model):
    """Author utilizando el listado de Users del sistema"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


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
        return "%s [    Inicio: %s  - Fin:  %s  ]" % (
            self.description,
            self.startdate,
            self.enddate,
        )


class JobGroup(models.Model):
    """Monto : JobGroup para Jobs listado  """

    jobgroup = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # breakpoint()
        # job = Job.objects.filter(jobgroup=f"{self.jobgroup}")
        job = Job.objects.filter(jobgroup=f"{self.id}")
        return "[    %s  Jobs ]: %s" % (len(job), self.jobgroup)
        # return self.jobgroup


class Job(models.Model):
    """Monto : Jobs listado  """

    jobrol = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    jobgroup = models.ForeignKey(JobGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "[    %s  ]: %s" % (self.jobgroup.jobgroup, self.jobrol)
        # return self.jobrol

class Donation(models.Model):
    """Info : del Donante"""

    firtsname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    # jobrol = models.CharField(max_length=40)

    createdate = models.DateTimeField(auto_now_add=True)
    jobrol = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation_Goal = models.ForeignKey(Donation_Goal, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.email)
    
class Collaboration(models.Model):
    """Monto : donado """

    donation = models.IntegerField()
    # jobrol = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.payment, self.createdate)
