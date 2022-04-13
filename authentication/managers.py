from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """User Manager."""

    def create_user(self, username=None, password=None):
        if not username:
            raise ValueError("Username field is required.")
        if not password:
            raise TypeError("User must have a password.")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user
