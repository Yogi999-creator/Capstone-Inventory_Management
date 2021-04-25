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

    choose = models.CharField(max_length=15, choices=choose, null=True, default='Supplier')
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    products = models.CharField(max_length=15, choices=products, null=True)
   