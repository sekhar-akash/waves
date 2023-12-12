from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince
# Create your models here.

def upload_to_directory(instance, filename):
    return f'posts/{instance.creator.username}/{filename}'

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
        return self.creator.full_name
    
    def total_likes(self):
        return self.likes.count()
    
class Comments(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s - %s' % (self.post.id,self.content, self.user.full_name)
    
    def created_time(self):
        return timesince(self.created)



class Follow(models.Model):
    follower = models.ForeignKey(get_user_model(),related_name='followers',on_delete=models.CASCADE)
    following = models.ForeignKey(get_user_model(),related_name='following',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower} -> {self.following}'