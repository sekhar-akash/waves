from rest_framework import serializers
from .models import Posts,Follow
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only = True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.total_likes()
    
    class Meta:
        model = Posts
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    follower = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    
    class Meta:
        model = Follow
        fields = ['follower', 'following']