from django.contrib import admin

from blog.models import (Tag, ResourceType, News, Resource)


class NewsModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'author']
    list_filter = ['date_created', 'date_modified']
    prepopulated_fields = {'slug': ('title',), }
    class Meta:
        model = News


class ResourceModelAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'author', 'tags']
    list_filter = ['date_created', 'date_modified']
    prepopulated_fields = {'slug': ('title',), }

    class Meta:
        model = Resource



admin.site.register(Tag)
admin.site.register(ResourceType)
admin.site.register(News, NewsModelAdmin)
admin.site.register(Resource, ResourceModelAdmin)

