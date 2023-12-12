from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import PostSerializer, FollowSerializer
from .models import Posts,Follow
from django.contrib.auth import get_user_model


User = get_user_model()

class CreatePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def post(self, request):
        print("form data",request.data)
        serializer = self.serializer_class(data=request.data)
        print("serializer",serializer)


        if serializer.is_valid():
            print('got here')
            post = serializer.save(creator=request.user)
            print("got second")
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Posts.objects.filter(is_deleted = False, is_blocked=False, creator__is_active=True).order_by('-created_at')
    serializer_class = PostSerializer


class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        try:
            post = Posts.objects.filter(id=pk)
            serializer = PostSerializer(post)
            return Response (serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    
    def post(self, request, pk):
        try:
            user = request.user
            follows = User.objects.get(id=pk)
            is_following = Follow.objects.filter(follower=user, following=follows).first()

            if is_following:
                is_following.delete()
                return Response({'message': 'Unfollowed Successfully', 'is_following': False}, status=status.HTTP_200_OK)
            else:
                new_follow = Follow(follower=user, following=follows)
                new_follow.save()
                return Response({'message': 'Followed Successfully', 'is_following': True}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class PostLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = request.user
            post = Posts.objects.get(pk=pk)
            if user in post.likes.all():
                post.likes.remove(user)
                liked_message = "Post unliked!"
                is_liked = False
            else:
                post.likes.add(user)
                liked_message = "Post liked!"
                is_liked = True

            total_likes = post.total_likes()  # Calculate total likes

            # Assuming you have a serializer for your Post model
            serializer = PostSerializer(post)

            return Response(
                {"message": liked_message, "total_likes": total_likes, "is_liked":is_liked, "post_data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Posts.DoesNotExist:
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


