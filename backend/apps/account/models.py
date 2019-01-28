from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser


class Belong(models.Model):
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
    id = models.AutoField(primary_key=True)
    name = models.CharField('学科', max_length=30)

    class Meta:
        db_table = 'departments'
        verbose_name_plural = '学科'
        verbose_name = '学科'

    def __str__(self):
        return self.name


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('学年', max_length=30)
    order = models.IntegerField('優先順位', unique=True)

    class Meta:
        db_table = 'grades'
        verbose_name_plural = '学年'
        verbose_name = '学年'

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, student_id, name, password=None, **extra_fields):
        if not student_id:
            raise ValueError('学籍番号は必須です.')
        user = self.model(student_id=student_id, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, student_id, name, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(student_id, name, **extra_fields)

    def create_superuser(self, student_id, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('belong_id', 1)
        extra_fields.setdefault('department_id', 1)
        extra_fields.setdefault('grade_id', 1)
        return self._create_user(student_id, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField('学籍番号', max_length=8, unique=True, help_text='8桁の学籍番号を入力してください.')
    name = models.CharField('名前', max_length=100, help_text='名前を入力してください.')
    belong = models.ForeignKey(Belong, on_delete=models.PROTECT, help_text='所属している局・部門を選択してください.')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, help_text='学科を選択してください.')
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, help_text='学年を選択してください.')
    phone_number = models.CharField('電話番号', max_length=11, blank=True, null=True,
                                    help_text='電話番号を入力してください(半角数字のみ).')
    is_leader = models.BooleanField('局長/部門長', default=False)
    is_subleader = models.BooleanField('副局長/副部門長', default=False)

    is_staff = models.BooleanField('スタッフ権限', default=False, help_text='管理画面にアクセスすることができる.')
    is_active = models.BooleanField('有効なユーザ', default=True, help_text='有効なユーザである.')
    is_superuser = models.BooleanField('スーパーユーザ権限', default=False, help_text='全ての権限を持っている.')

    objects = UserManager()

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'ユーザ'
        verbose_name = 'ユーザ'

    def __str__(self):
        return self.name
