from django.contrib import admin
from .models import Post,Comment
from django.utils.text import slugify

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'status')
    list_display = ('title', 'author', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    actions = ['publish_post']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

    def publish_post(self, request, queryset):
        queryset.update(status=1)

admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commented_by', 'message', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('message',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)