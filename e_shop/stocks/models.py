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
        ('XXL+', 'Double Extra Large+'),
    ]
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    FABRIC_CHOICES = [
        ('cotton', 'Cotton'),
        ('polyester', 'Polyester'),
        ('lycra', 'Lycra'),
    ]
    fabric = models.CharField(max_length=20, choices=FABRIC_CHOICES)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ImgStocks(models.Model):

    stocks = models.ForeignKey(Stock, on_delete=CASCADE)
    img = models.ImageField(upload_to="stock_img")


class Purchase(models.Model):

    address = models.CharField()
    phone = models.IntegerField()
    email = models.EmailField()
    product = models.ForeignKey(Stock, on_delete=CASCADE)
    completed = models.BooleanField(default=False)


