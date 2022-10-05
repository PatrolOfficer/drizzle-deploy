from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ['title','author', 'date_posted','tag_list']

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
