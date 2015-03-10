from django.contrib import admin
from nodes.models import Node, Tag


class NodeAdmin(admin.ModelAdmin):
    list_display = ['myuser', 'title', 'post', ]

admin.site.register(Node, NodeAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'article']

admin.site.register(Tag, TagAdmin)

# Register your models here.
