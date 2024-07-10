import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import (
    models,
    transaction,
)
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        with transaction.atomic():
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserModel(AbstractUser):
    email = models.EmailField(unique=True, verbose_name=_('Email'))

    first_name = models.CharField(max_length=256, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=256, verbose_name=_('Last Name'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = None

    objects = CustomUserManager()

    def to_entity(self) -> User:
        return User(
            id=self.id,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
        )
