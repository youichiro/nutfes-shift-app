from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('メールアドレスは必須です.')
        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, **extra_fields)

    def create_superuser(self, name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', unique=True)

    is_staff = models.BooleanField('Staff', default=False, help_text='管理画面にアクセスできるかどうか')
    is_active = models.BooleanField('Active', default=True, help_text='有効なユーザかどうか')
    is_superuser = models.BooleanField('SuperUser', default=False, help_text='全ての権限を持っているかどうか')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'ユーザ'
        verbose_name = 'ユーザ'

    def __str__(self):
        return self.name
