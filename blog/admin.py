from django.contrib import admin
from .models import Post,Category,Comment,Notification,Photo,Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Notification)
admin.site.register(Tag)