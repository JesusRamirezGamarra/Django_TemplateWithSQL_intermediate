from django.contrib import admin
from .models import Author, Category, Post, Donation_Goal, JobGroup, Job ,Suscripcion, Perfil, PostUserColaborator,UserColaborator
from .forms import UserColaboratorForm
from django import forms

admin.site.empty_value_display = '(None)'
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Donation_Goal)
admin.site.register(JobGroup)
admin.site.register(Job)
admin.site.register(Suscripcion)
admin.site.register(Perfil)



@admin.register(UserColaborator)
class UserColaboratorAdmin(admin.ModelAdmin):
    # empty_value_display = 'unknown'
    form = UserColaboratorForm    
    list_display = ['id','email','user']    
    
    # list_display = ['username','pwd']
    # fields = (("username", "pwd"))
    
    # @admin.display(empty_value='unknown')
    # def username(self, obj):
    #     return obj.username    
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # form.base_fields["name"].label = "Full Name"
        # form.base_fields["username"].label = "User Name"
        # form.base_fields["pwd"].label = "Password"
        form.base_fields["profile_picture"].label = "profile Image"
        form.base_fields["user"].label = "Usuario Django"
        return form          
# #admin.site.register(UserColaborator,UserColaboratorAdmin)   # otra forma de relacionar con model y form.

@admin.register(PostUserColaborator)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','title']
    

admin.site.site_header  =  "Best Friend Forever (BFF) -  admin"  
admin.site.site_title  =  "BFF admin site"
admin.site.index_title  =  "BFF Admin"