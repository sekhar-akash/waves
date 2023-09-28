from django.urls import path
from .views import RegisterView,RetrieveUserView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('user', RetrieveUserView.as_view(), name='register'),

]
