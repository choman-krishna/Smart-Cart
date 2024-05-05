from django.db import models

class ItemData(models.Model):
    item_name = models.TextField(max_length=20)
    bar_data = models.TextField(max_length=40)
    prize = models.DecimalField(max_digits=10, decimal_places=2)
    item_img = models.ImageField(upload_to = 'item_img/', max_length = 300, null=True, default = None)

# Create your models here.
