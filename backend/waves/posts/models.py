from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

def upload_to_directory(instance, filename):
    return f'posts/{instance.user.username}/{filename}'

class Posts(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to=upload_to_directory)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)
    is_deleted = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.creator
    
class Comments(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)