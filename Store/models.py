from django.db import models

# Create your models here.
class User(models.Model):
    choose= [
    ('Supplier', 'Supplier'),
    ('Buyer', 'Buyer'),
    ]

    products= [
    ('Pen', 'Pen'),
    ('NoteBook', 'NoteBook'),   
    ]
    sr_number = models.IntegerField()
    choose = models.CharField(max_length=15, choices=choose, null=True, default='Supplier')
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=1000)
    products = models.CharField(max_length=15, choices=products, null=True, default="Pen")
    quantity = models.FloatField()
    packaging = models.BooleanField()
    date = models.DateField(default="2021-04-27")
    images = models.ImageField(upload_to='images/',default="")
   