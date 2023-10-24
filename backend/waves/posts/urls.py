from . import views
from django.urls import path

urlpatterns = [
    path('create-post/',views.CreatePostView.as_view(),name="create-post")
]
