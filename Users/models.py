from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_company=models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_admin= models.BooleanField(default=False)


    def has_perm(self ,perm, obj=None):
        return True

    def has_moduleperm(self, app_label):
        return True



    objects = CustomUserManager()

    def __str__(self):
        return self.email
