from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ScrapProduct(models.Model):
    query_id = models.IntegerField()
    query_date = models.DateTimeField(auto_now_add=True)
    product_query_name = models.CharField(max_length=200)
    product_scrap_name = models.CharField(max_length=200)
    product_link = models.CharField(max_length=200)
    product_link_img = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_country = models.CharField(max_length=200)
    product_quality = models.CharField(max_length=200)
    user_name = models.CharField(max_length=70)
    product_platform = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.product_platform} — {self.product_query_name} — {self.product_price}'


class Item(models.Model):
    country = models.CharField(max_length=255)
    delivery_time_days = models.IntegerField()
    delivery_time_text = models.CharField(max_length=255)

    def __str__(self):
        return self.country
