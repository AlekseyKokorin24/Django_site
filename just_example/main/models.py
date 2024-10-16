from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    preview = models.CharField(max_length=250, verbose_name="Предпросмотр")
    content = models.TextField(verbose_name="Содержание")
    published = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, db_index=True)

class User(models.Model):
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    password = models.CharField(max_length=50, verbose_name='Пароль')