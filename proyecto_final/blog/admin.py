from django.contrib import admin
from .models import Author, Category, Post, Donation_Goal, JobGroup, Job ,Suscripcion, Perfil, PostUserColaborator,UserColaborator
from .forms import UserColaboratorForm
# from django import forms

admin.site.site_header  =  "Best Friend Forever (BFF) -  admin"  
admin.site.site_title  =  "BFF admin site"
admin.site.index_title  =  "BFF Admin"
admin.site.empty_value_display = '(None)'

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ['__str__']
    ordering = ['user']
    search_fields = ['user']
    date_hierarchy = 'created'
    list_filter = ('created','user')    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created','title','subtitle']    
    list_display = ('title','subtitle')
    ordering = ('title', 'subtitle')
    search_fields = ('title','subtitle')    
    date_hierarchy = 'created'
    list_filter = ('created','title')  
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['timestamp','created','updated']    
    list_display = ('author','title','post_categories','featured')
    ordering = ('author', 'title','featured')
    search_fields = ('author','title','featured')    
    date_hierarchy = 'created'
    list_filter = ('created','author','featured')    
    def post_categories(self, obj):
        return ", ".join(
            [c.title for c in obj.categories.all().order_by("title")])
    post_categories.short_description = "Categorías"    
    
    
@admin.register(Donation_Goal)
class Donation_GoalAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ('description','goal','startdate','enddate','active')
    ordering = ('description', 'goal','startdate','enddate','active')
    search_fields = ('description','goal','startdate','enddate','active')
    date_hierarchy = 'created'
    list_filter = ('created','description','goal','active')    


@admin.register(JobGroup)
class JobGroupAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ['name']
    ordering = ['name']
    search_fields =  ['name']
    date_hierarchy = 'created'
    list_filter = ['created']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ['name','jobgroup']
    ordering = ['name','jobgroup']
    search_fields =  ['name','jobgroup']
    date_hierarchy = 'created'
    list_filter = ['created','jobgroup']


@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ['name']
    ordering = ['name']
    search_fields =  ['name']
    date_hierarchy = 'created'
    list_filter = ['created']


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ['name']
    ordering = ['name']
    search_fields =  ['name']
    date_hierarchy = 'created'
    list_filter = ['created']


@admin.register(UserColaborator)
class UserColaboratorAdmin(admin.ModelAdmin):
    form = UserColaboratorForm    
    readonly_fields = ['createdate','created','updated']
    list_display = ['user','perfil','email']    
    ordering = ('user', 'perfil','email')
    search_fields = ('user','perfil','email')    
    date_hierarchy = 'createdate'
    list_filter = ('created','user','perfil')
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["profile_picture"].label = "Avatar"
        form.base_fields["user"].label = "Usuario"
        return form        
# admin.site.register(UserColaborator)    # relacion con valores por default usando models.
# admin.site.register(UserColaborator,UserColaboratorAdmin)   # otra forma de relacionar con model y form.