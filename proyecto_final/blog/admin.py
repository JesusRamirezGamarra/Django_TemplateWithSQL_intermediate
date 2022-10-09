from django.contrib import admin
from .models import Author, Category, Post,Donation_Goal,JobGroup,Job
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Donation_Goal)
admin.site.register(JobGroup)
admin.site.register(Job)