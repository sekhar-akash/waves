from . import views
from django.urls import path

urlpatterns = [
    path('create-post/',views.CreatePostView.as_view(),name="create-post"),
    path('post-list/',views.PostListView.as_view(),name='post-list'),
    path('post-detail/<str:pk>',views.PostDetailView.as_view(), name='post-detail'),
    path('follow-user/<int:pk>/',views.FollowUserView.as_view(), name='follow'),
    path('like-post/<int:pk>/',views.PostLikeView.as_view(),name="like-post"),
]
