from django.db import models
from django.utils import timezone


class Blogs(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    preview = models.CharField(max_length=450, verbose_name="Предпросмотр")
    content = models.TextField(verbose_name="Содержание")
    published = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
class User(models.Model):
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    password = models.CharField(max_length=50, verbose_name='Пароль')

