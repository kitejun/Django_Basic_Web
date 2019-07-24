from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'image')
    
admin.site.register(Board, BoardAdmin)

admin.site.register(Comment)