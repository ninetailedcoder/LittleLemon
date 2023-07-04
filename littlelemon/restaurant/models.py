from django.db import models

# Create your models here.
class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(max_length=10)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
class booking(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()
    bookingDate = models.DateTimeField()
    def __str__(self):
        return self.name