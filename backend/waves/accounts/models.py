from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")

        if not username:
            raise ValueError("User must have an user name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def upload_to(instance, filename):
    return 'profile/{filename}'.format(filename=filename)



class UserAccount(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=100,blank=True,null=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=30,null=True,blank=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to=upload_to, default='user.png')

    date_joined = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    last_login = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    