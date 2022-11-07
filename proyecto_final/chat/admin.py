from django.contrib import admin
from .models import Room, Message

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ['name']
    ordering = ['name']
    search_fields =  ['name']
    date_hierarchy = 'created'
    list_filter = ['created']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']    
    list_display = ['user','length_message_']
    ordering = ['user']
    search_fields =  ['user']
    date_hierarchy = 'created'
    list_filter = ['created']
    def length_message_(self, obj):
        return len( str(obj.value))
    length_message_.short_description = "# de caracteres"  