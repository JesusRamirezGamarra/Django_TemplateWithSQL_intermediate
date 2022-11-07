from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User 


# Create your models here.
User = get_user_model()
class Author(models.Model):
    """Author: utilizado el listado de Users del sistema(FK) utilizando para publicar los POST generales del BLOG"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return f"""{self.user.first_name} {self.user.last_name} """
    class  Meta:
        verbose_name = "Autor"
        verbose_name_plural  =  "Author [ Autor ]"    


class Category(models.Model):
    """Category: utilizado para determinar las categorias que agrupan los POST generales del BLOG"""
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        post_lenght= Post.objects.filter(categories=self.id).count()
        return f"""{self.title}  [ {post_lenght} ] """
    class  Meta:
        verbose_name = "Categoria"
        verbose_name_plural  =  "Category [ Categoria ]"        


class Post(models.Model):
    """Post: Utilizado para contener la informacion minima solicitada que debe contener un POST """
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()   
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return self.title
    class  Meta:
        verbose_name = "Publicación"
        verbose_name_plural  =  "Post [ Publicación ]"            
        

class JobGroup(models.Model):
    """JobGroup: Utilizado como agrupador de Jobs """
    name = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        job = Job.objects.filter(jobgroup=f"{self.id}")
        return "[    %s  Jobs ]: %s" % (
            len(job), 
            self.name
        )
    class  Meta:
        verbose_name = "Grupo de trabajo"
        verbose_name_plural  =  "JobGroup [ Grupo de trabajo ]"    


class Job(models.Model):
    """Job : Utilizado para contener el listado de Job """
    name = models.CharField(max_length=40)
    createdate = models.DateTimeField(auto_now_add=True)
    jobgroup = models.ForeignKey(JobGroup, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return "[   ID-%s  ]-[    %s  ]: %s" % (
            self.id,
            self.jobgroup.name, 
            self.name
        )
    class  Meta:
        verbose_name = "Trabajo"
        verbose_name_plural  =  "Job [ Trabajo ]"            


class Donation_Goal(models.Model):
    """Donation_Goal : Utilizado para contener la informacion requerida para cumplir con el Objetivo de Donacion"""
    goal = models.IntegerField()
    description = models.CharField(max_length=500)
    startdate = models.DateField()
    enddate = models.DateField()
    active = models.BooleanField()
    createdate = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        activo =  "Activo" if self.active else "Inactivo"
        return "%s : [    Inicio: %s  - Fin:  %s  ] %s " % (
            activo,
            self.startdate,
            self.enddate,
            self.description,
        )
    class  Meta:
        verbose_name = "Meta:Donacion"
        verbose_name_plural  =  "Donation_Goal [ Meta:Donacion ]"         
        

class Donation(models.Model):
    """Donation : Utilizando para contener la informacion del Donante"""
    firtsname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    createdate = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation_Goal = models.ForeignKey(Donation_Goal, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return "%s %s  : [ %s ]" % (
            self.firtsname,
            self.firtsname, 
            self.email
        )
    class  Meta:  
        verbose_name = "Donacion"
        verbose_name_plural  =  "Donation [ Donacion ]" 

    
class Collaboration(models.Model):
    """Collaboration : Utilizando para contener la informacion de monto colaborado"""
    amount  = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return "%s %s" % (self.amount, self.createdate)
    class  Meta:  
        verbose_name = "Colaboracion"
        verbose_name_plural  =  "Collaboration [ Colaboracion ]"     
    
    
class Embrace(models.Model):
    """Embrace : Utilizado para contener informacion del potecial Adoptante"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return "%s %s" % (self.name, self.email)
    class  Meta:  
        verbose_name = "Adoptar"
        verbose_name_plural  =  "Embrace [ Adoptar ]"
        
    
class Contact(models.Model):
    """Contact : Formulario de Conactanos"""
    name = models.CharField(max_length=50)    
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return "%s %s %s" % (self.name, self.email, self.subject)
    class  Meta:
        verbose_name = "Contáctanos"
        verbose_name_plural  =  "Contact [ Contáctanos ]"
        

class Suscripcion(models.Model):
    """Suscripcion : Utilizado para contener el listado de suscripciones"""
    name = models.CharField(max_length=50)    
    createdate = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return self.name
    class  Meta:   
        verbose_name = "Suscripción"
        verbose_name_plural  =  "Subscription [ Suscripción ]"
        
    
class Perfil(models.Model):
    """Perfil : Utilizando para contener el listado de Perfil(es) """    
    name = models.CharField(max_length=50)    
    createdate = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)         
    def __str__(self):
        return self.name
    class  Meta:
        verbose_name = "Perfil"
        verbose_name_plural  =  "Perfil [ Perfil ]"
        

class UserColaborator(models.Model):
    """UserColaborator : Utilizando para contener el listado de User Colaborator"""        
    email = models.EmailField(max_length=200)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to ='avatar',max_length=None, blank=True,null=True)
    perfil= models.ForeignKey(Perfil, on_delete=models.CASCADE, default=1 )
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, default=1)
    createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)        
    def __str__(self):
        return  f""" {self.email}  """
    class  Meta:
        verbose_name = "User:Colaborador"
        verbose_name_plural  =  "UserColaborator [User:Colaborador]"   
        

class PostUserColaborator(models.Model):
    """PostUserColaborator : Utilizando para contener el contenido de un POST realizado por un User Colaborator"""   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True,null=True)#
    createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)           
    def __str__(self):
        return self.title
    class  Meta:
        verbose_name = "Publicación:User:Colaborador"
        verbose_name_plural  =  "PostUserColaborator [Publicación:User:Colaborador]"    