from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce import models as tiny_models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = tiny_models.HTMLField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    def get_date(self):
        time = timezone.now()
        if self.created_on.day == time.day:
            if self.created_on.minute == time.minute:
                return str(time.second - self.created_on.second) + " seconds ago"
            if self.created_on.hour == time.hour:
                return str(time.minute - self.created_on.minute) + " minutes ago"
            return str(time.hour - self.created_on.hour) + " hours ago"
        if self.created_on.year == time.year:
            if self.created_on.month == time.month:
                return str(time.day - self.created_on.day) + " days ago"
            return str(time.month - self.created_on.month) + " months ago"
        if self.created_on.year <= time.year:
            return str(time.year - self.created_on.year) + " years ago"
        return self.created_on

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comments')
    commented_by = models.ForeignKey(User, default='', on_delete=CASCADE, related_name='user_comments')
    message = models.TextField(max_length=200)
    reply_of = models.ForeignKey('self', on_delete=models.CASCADE,default=None, null=True, related_name='replies')
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    def get_date(self):
        time = timezone.now()
        if self.created_on.day == time.day:
            if self.created_on.minute == time.minute:
                return str(time.second - self.created_on.second) + " seconds ago"
            if self.created_on.hour == time.hour:
                return str(time.minute - self.created_on.minute) + " minutes ago"
            return str(time.hour - self.created_on.hour) + " hours ago"
        if self.created_on.year == time.year:
            if self.created_on.month == time.month:
                return str(time.day - self.created_on.day) + " days ago"
            return str(time.month - self.created_on.month) + " months ago"
        if self.created_on.year <= time.year:
            return str(time.year - self.created_on.year) + " years ago"
        return self.created_on

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.message, self.commented_by.username)

