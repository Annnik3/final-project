from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, birth_date=None, personal_number=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            birth_date=birth_date,
            personal_number=personal_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, birth_date=None, personal_number=None):
        user = self.create_user(email, username, password, birth_date, personal_number)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    personal_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    # This is for authenticating users with email and not username
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
