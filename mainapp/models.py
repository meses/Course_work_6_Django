from django.db import models

NULLABLE = {'blank': True, 'null': True}

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.EmailField(max_length=50, verbose_name='email')
    description = models.CharField(max_length=256, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'Имя: {self.name}, email: {self.email}, Описание: {self.description}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('id',)


class Message(models.Model):
    message_title = models.CharField(max_length=100, verbose_name='Тема письма')
    message_body = models.TextField(max_length=2000, verbose_name='Тело письма')

    def __str__(self):
        return f'{self.message_title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('id',)


class SendingStatus(models.Model):
    status_name = models.CharField(max_length=16, verbose_name='Статус')

    def __str__(self):
        return f'{self.status_name}'

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'
        ordering = ('id',)

class Periodicty(models.Model):
    per_name = models.CharField(max_length=16, verbose_name='Периодичность')

    def __str__(self):
        return f'{self.per_name}'

    class Meta:
        verbose_name = 'периодичность'
        verbose_name_plural = 'периодичность'
        ordering = ('id',)


class SendingSettings(models.Model):
    sending_time = models.TimeField(verbose_name='Время рассылки')
    periodicity_id = models.ForeignKey('Periodicty', verbose_name='Периодичность', on_delete=models.PROTECT)
    message_id = models.ForeignKey('Message', verbose_name='Сообщение', on_delete=models.PROTECT)
    status_id = models.ForeignKey('SendingStatus', verbose_name='Статус', on_delete=models.PROTECT)
    client_id = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.CASCADE)

    def __str__(self):
        return f'Клиенту: {self.client_id} в {self.sending_time} с периодичностью {self.periodicity_id} посылаем сообщение {self.message_id}. Статус рассылки: {self.status_id}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('id',)

class SendingLog(models.Model):
    recipient_id = models.ForeignKey('SendingStatus', verbose_name='Рассылка', on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now=True, verbose_name='Время попытки')
    attempt_status = models.BooleanField(verbose_name='Статус попытки')
    server_response = models.CharField(max_length=256, verbose_name='Ответ сервера', **NULLABLE)

    def __str__(self):
        return f'Рассылка {self.recipient_id} в {self.attempt_time} имеет статус {self.attempt_status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('id',)
