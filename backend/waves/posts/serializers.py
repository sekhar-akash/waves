from rest_framework import serializers
from .models import Posts,Follow,Comments
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    
    class Meta:
        model = Comments
        fields = ['id','user','body','created_time']


class PostSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only = True)
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many = True,read_only = True)

    def get_likes_count(self, obj):
        return obj.total_likes()
    
    class Meta:
        model = Posts
        fields = '__all__'
        extra_fields = ['comments']


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    follower = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    
    class Meta:
        model = Follow
        fields = ['follower', 'following']


