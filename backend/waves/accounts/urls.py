from django.urls import path
from .views import RegisterView,RetrieveUserView,UpdateUserView,AdminUsersList,UsersList,BlockUser,PostsList

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', RetrieveUserView.as_view(), name='register'),
    path('update/',UpdateUserView.as_view(),name='update'),
    path('userslist/',UsersList.as_view(),name='userslist'),
    path('adminuserslist/',AdminUsersList.as_view(), name='adminuserslist'),
    path('blockuser/<str:id>',BlockUser.as_view(),name='blockuser'),
    path('postslist/',PostsList.as_view(),name="postslist")

]
