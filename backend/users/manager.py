from django.contrib.auth.base_user import BaseUserManager
from .utils import logger


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """ """
        if not email:
            logger.error("ValueError: Email must be set ")
            raise ValueError("The Email Must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_staff") is not True:
            logger.error("is_staff should be set to True for superuser")
            raise ValueError("is_staff should be set to True for superuser")
        if extra_fields.get("is_superuser") is not True:
            logger.info("is_superuser should be set to True for superuser")
            raise ValueError("is_superuser should be set to True for superuser")
        self.create_user(email, password, **extra_fields)
