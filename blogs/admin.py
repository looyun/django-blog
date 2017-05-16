from django.contrib import admin

# Register your models here.
from .models import Article,Comment,MyUser

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edit_date')

    list_filter = ['pub_date']
    
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','content','user','pub_date')

    list_filter = ['pub_date']
    
    search_fields = ['content']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(MyUser)