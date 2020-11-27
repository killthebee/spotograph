from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Spot(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название Спота')
    description = models.TextField(verbose_name='Короткое описание', default='Дефолтное описание спота...')
    features = HTMLField(default='Дефолтное описание фитч спота...', verbose_name='Длинное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    inst = models.CharField(max_length=50, verbose_name='Ссылка на инсту', blank=True)
    vk = models.CharField(max_length=50, verbose_name='Ссылка на вк', blank=True)
    owner = models.ForeignKey(User,
                              verbose_name='Владелец',
                              on_delete=models.CASCADE,
                              related_name='spots',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Спот'
        verbose_name_plural = 'Споты'


class MainImage(models.Model):
    main_image = models.ImageField(verbose_name='Верхняя картинка', upload_to='main_images/')
    spot = models.OneToOneField(Spot, on_delete=models.CASCADE, verbose_name='Спот', related_name='main_image')

    def __str__(self):
        return f"{self.id} lel"

    class Meta:
        verbose_name = 'Главное изображение'
        verbose_name_plural = 'Главные изображения'


class FeatureImage(models.Model):

    place = models.ForeignKey(Spot, on_delete=models.CASCADE, verbose_name='Спот', related_name='images')
    image = models.ImageField(verbose_name='Изображение фитч', upload_to='features_images/')

    def __str__(self):
        return f'Изображение {self.id}.{self.place.title}'

    class Meta:
        verbose_name = 'Изображение фитч спота'
        verbose_name_plural = 'Изображения фитч спота'


class ChatMessage(models.Model):
    text = models.TextField('Текст')
    time = models.DateTimeField('ДатаВремя', auto_now_add=True)
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    spot = models.ForeignKey(
        Spot,
        verbose_name='Спот',
        on_delete=models.CASCADE,
        related_name='messages'
    )

    def __str__(self):
        return f'Сообщение от {self.user.username}№{self.id}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['time']
