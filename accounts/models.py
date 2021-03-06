from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email,full_name=None, password = None, is_active=True, is_staff = False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    def create_staffuser(self,email,full_name=None, password=None):
        user =self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None,password=None):
        user =self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin =True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(blank = True, max_length=50, null = True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    # notice the absence of a "Password field", that is built in.


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    objects = UserManager()
    def get_full_name(self):
        # The user is identified by their email address
        if self.full_name:
            return self.full_name
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class GuestMail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    