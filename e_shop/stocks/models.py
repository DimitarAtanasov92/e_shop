from django.db import models
from django.db.models import CASCADE


class Stock(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    TYPE_CHOICES = [
        ('suit', 'Suit'),
        ('blouse', 'Blouse'),
        ('t-shirt', 'T-Shirt'),
        ('skirt', 'Skirt'),
        ('pants', 'Pants'),
        ('skirt_suit', 'Skirt Suit'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    SIZE_CHOICES = [
        ('L', 'Large'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('quick', 'My Choice is Quick'),
    ]
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    FABRIC_CHOICES = [
        ('cotton', 'Cotton'),
        ('polyester', 'Polyester'),
        ('lycra', 'Lycra'),
    ]
    fabric = models.CharField(max_length=20, choices=FABRIC_CHOICES)

    def __str__(self):
        return self.name


class ImgStocks(models.Model):

    stocks = models.ForeignKey(Stock, on_delete=CASCADE)
    img = models.ImageField()
