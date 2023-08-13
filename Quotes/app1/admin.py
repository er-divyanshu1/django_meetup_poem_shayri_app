from django.contrib import admin
from .models import Category, Post, Reader

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','decription','url','date',)

class PostAdmin(admin.ModelAdmin):
    list_display=('cat','Content',)
    list_filter=('cat',)

class ReaderAdmin(admin.ModelAdmin):
    list_display=('name','email',)
    list_filter=('userdate',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Reader,ReaderAdmin)

