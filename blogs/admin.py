from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edit_date')

    list_filter = ['pub_date']
    
    search_fields = ['title']

admin.site.register(Article,ArticleAdmin)