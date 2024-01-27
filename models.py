from django.db import models


class Apartment(models.Model):
    login = models.CharField(max_length=200, verbose_name="Логин Владельца")
    city = models.CharField(max_length=200, verbose_name="Город")
    street = models.CharField(max_length=300, verbose_name="Улица")
    house_number = models.CharField(max_length=100, verbose_name="Номер дома")
    building_number = models.CharField(max_length=100, verbose_name="Номер корпуса", blank=True)
    apart_number = models.CharField(max_length=100, verbose_name="Номер квартиры", blank=True)
    select_stuff = models.CharField(max_length=500, verbose_name="Обслуживание", blank=True)
    select_admin = models.CharField(max_length=500, verbose_name="Администрирование", blank=True)
    insructions = models.TextField(verbose_name="Инструкции", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = 'Апартаменты'
        verbose_name_plural = 'Апартаменты'

class Booking(models.Model):
    start_date = models.DateField(verbose_name="Дата заезда")
    end_date = models.DateField(verbose_name="Дата выезда")
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="bookings")
    booking_platform = models.CharField(max_length=500, verbose_name="Платформа бронирования", blank=True)
    guest_name = models.CharField(max_length=300, verbose_name="Имя гостя", blank=True)
    phone = models.CharField(max_length=100, verbose_name="Номер телефона гостя", blank=True)
    prepayment = models.IntegerField(verbose_name="Размер предоплаты", blank=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
