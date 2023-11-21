from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, name, password, **kwargs):
        if not kwargs["email"]:
            raise ValueError("Вы не предоставили действительный e-mail")
        name = name.lower()
        kwargs["email"] = kwargs["email"].lower()
        kwargs["email"] = self.normalize_email(kwargs["email"])
        user = self.model(name=name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, password=None, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)
        return self._create_user(name, password, **kwargs)

    def create_superuser(self, name=None, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        return self._create_user(name, password, **kwargs)


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        blank=True,
        default="",
        unique=True,
        verbose_name="email",
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        default="",
        unique=True,
        verbose_name="Пользователь",
    )

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    """ !!! """
    # email - аутентификация через email
    # name - аутентификация через имя

    USERNAME_FIELD = "name"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    """ !!! """

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split("@")[0]
