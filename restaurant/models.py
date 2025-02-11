from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    inventory = models.PositiveIntegerField() 

    def __str__(self):
        return f'{self.title} : {str(self.price)}'  # исправлен метод __str__()

class Booking(models.Model):
    name = models.CharField(max_length=255) 
    no_of_guests = models.PositiveIntegerField()  
    booking_date = models.DateTimeField()  

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"