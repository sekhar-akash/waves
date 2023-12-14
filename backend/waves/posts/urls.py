from . import views
from django.urls import path

urlpatterns = [
    path('create-post/',views.CreatePostView.as_view(),name="create-post"),
    path('post-list/',views.PostListView.as_view(),name='post-list'),
    path('home-posts/',views.PostHomeView.as_view(),name='home-posts'),
    path('post-detail/<int:pk>',views.PostDetailView.as_view(), name='post-detail'),
    path('follow-user/<int:pk>/',views.FollowUserView.as_view(), name='follow'),
    path('like-post/<int:pk>/',views.PostLikeView.as_view(),name="like-post"),
    path('create-comment/<int:pk>/',views.PostCommentView.as_view(),name='create-comment'),
    path('delete-comment/<int:pk>/',views.DeleteCommentView.as_view(),name='delete-comment')
]
