from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
    def create_user(self, email, phone, username, password=None):
        if not email:
            raise ValueError('У пользователей должен быть адрес электронной почты.')
        if not phone:
            raise ValueError('У пользователей должен быть номер телефона.')
        if not username:
            raise ValueError('У пользователей должно быть имя пользователя.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, username, password):
        user = self.create_user(
            phone=phone,
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, blank=True, unique=True)
    username = models.CharField(max_length=30, unique=True,  verbose_name='Имя пользователя')
    phone = models.CharField(max_length=255, unique=True, verbose_name='Номер телефона')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']

    objects = MyAccountManager()

    def __str__(self):
        return f"{self.username},{self.email},{self.phone}"

    # For checking permissions. to keep it simple all admin have ALL permissons. Для проверки разрешений. для
    # простоты у всех админов есть ВСЕ разрешения.
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY).Есть ли у этого пользователя
    # разрешение на просмотр этого приложения? (ВСЕГДА ДА ДЛЯ ПРОСТОТЫ)
    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# {
# "email": "khalilov@mail.ru",
# "username": "Blackbrother24",
# "phone": "+996999699026",
# "password": "qwerty12345",
# "password2": "qwerty12345"
# }


# class User(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Имя пользователя')
#     email = models.EmailField()
#     phone = models.CharField(max_length=255, verbose_name='Номер телефона')
#     login = models.CharField(max_length=255, verbose_name='Логин')
#     password = models.CharField(max_length=255, verbose_name='Пароль')
#     password2 = models.CharField(max_length=255, verbose_name='Пароль подтверждения')
#
#     def __str__(self):
#         return self.name
