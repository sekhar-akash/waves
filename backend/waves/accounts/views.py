from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer,UserSerializer
from django.contrib.auth import get_user_model
from posts.models import Posts
from posts.serializers import PostSerializer


User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data

        serializer = UserCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)

        return Response(user.data,status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)
    
class UpdateUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request):
        try:
            user = request.user
            user_obj = User.objects.get(pk=user.id)
            serializer = self.serializer_class(user_obj,data=request.data,partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response("User not found in the database.", status=status.HTTP_404_NOT_FOUND)
        

class UsersList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        try:
            user = User.objects.filter(is_admin = False).order_by('-date_joined')
            serializer = UserSerializer(user, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

#Admin- Users List

class AdminUsersList(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self,request):
        try:
            user = User.objects.filter(is_admin = False).order_by('-date_joined')
            serializer = UserSerializer(user, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


#Admin - Block User

class BlockUser(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self,request,id):
        try:
            user = User.objects.get(id=id)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()

            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PostsList(APIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get(self,request):
        try:
            posts = Posts.objects.all().order_by('-created_at')
            serializer = PostSerializer(posts, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
