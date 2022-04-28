from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


from django.db.models.deletion import DO_NOTHING

from authentication.managers import UserManager


class Role(models.Model):
    """User role model"""

    CUSTOMER = 1
    SUPPORT = 3

    ROLES_CHOICES = ((CUSTOMER, "Customer"), (SUPPORT, "Support"))

    id = models.PositiveIntegerField(primary_key=True, choices=ROLES_CHOICES)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser, PermissionsMixin):
    """User model"""
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, db_index=True, unique=True, null=False, blank=False)
    role = models.ForeignKey(Role, on_delete=DO_NOTHING, default=Role.CUSTOMER)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_username(self):
        return f"{self.email}"
