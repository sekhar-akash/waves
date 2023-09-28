from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self,username,full_name,phone ,email,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        email = email.lower()
        
        user = self.model(
            username = username,
            email = email,
            phone=phone,
            full_name=full_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email ,password=None):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class UserAccount(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=100,blank=True,null=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=30,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email
    