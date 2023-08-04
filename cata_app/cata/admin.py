from django.contrib import admin
from .models import Publisher, Publication, Article, Author, Edition, Tag
# Register your models here.

admin.site.register(Publisher)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Edition)
admin.site.register(Tag)
admin.site.register(Author)