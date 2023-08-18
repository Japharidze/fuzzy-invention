from django.db import models

class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    input_date = models.DateTimeField()
    lot_expiration_date = models.DateTimeField()
    lot_cnt = models.IntegerField()
    lot_cnt_current = models.IntegerField()
    manufacturer_name = models.CharField(max_length=50)
    manufacturer_icon_url = models.URLField()
    manufacturer_url = models.URLField()
    delivery_info = models.TextField(max_length=500)
    delivery_name = models.CharField(max_length=50)
    delivery_icon = models.URLField()
    delivery_url = models.URLField()
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

