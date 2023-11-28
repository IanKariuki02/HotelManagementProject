from django.db import models
from django.utils import timezone


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)


class Reservation(models.Model):
    reservation_number = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField(max_length=255)
    guest_phone_number = models.CharField(max_length=20)
    number_of_guests = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, **kwargs):
        # Calculate the total cost based on the room price and number of nights
        days = (self.check_out_date - self.check_in_date).days
        self.total_cost = self.room.price_per_night * days
        super().save(**kwargs)
