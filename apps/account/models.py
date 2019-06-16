from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser


class Belong(models.Model):
    """部署モデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('局・部門', max_length=30)
    short_name = models.CharField('局・部門(略称)', max_length=30)
    color = models.CharField('局・部門カラー', max_length=30, default='black')
    order = models.IntegerField('優先順位', unique=True)

    class Meta:
        db_table = 'belongs'
        verbose_name_plural = '部署'
        verbose_name = '部署'

    def __str__(self):
        return self.name


class Department(models.Model):
    """学科モデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('学科', max_length=30)

    class Meta:
        db_table = 'departments'
        verbose_name_plural = '学科'
        verbose_name = '学科'

    def __str__(self):
        return self.name


class Grade(models.Model):
    """学年モデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('学年', max_length=30)
    order = models.IntegerField('優先順位', unique=True)

    class Meta:
        db_table = 'grades'
        verbose_name_plural = '学年'
        verbose_name = '学年'

    def __str__(self):
        return self.name


class Member(models.Model):
    """局員モデル"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', unique=True)
    student_id = models.CharField('学籍番号', max_length=8, unique=True)
    belong = models.ForeignKey(Belong, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    is_leader = models.BooleanField('局長/部門長', default=False)
    is_subleader = models.BooleanField('副局長/副部門長', default=False)

    class Meta:
        db_table = 'members'
        verbose_name_plural = '局員'
        verbose_name = '局員'

    def __str__(self):
        return self.name


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

    is_staff = models.BooleanField('スタッフ権限', default=False, help_text='管理画面にアクセスすることができる.')
    is_active = models.BooleanField('有効なユーザ', default=True, help_text='有効なユーザである.')
    is_superuser = models.BooleanField('スーパーユーザ権限', default=False, help_text='全ての権限を持っている.')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'ユーザ'
        verbose_name = 'ユーザ'

    def __str__(self):
        return self.name
