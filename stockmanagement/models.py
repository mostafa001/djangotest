from django.db import models

# Create your models here.

# Table where the data will be saved

class Stock(models.Model):
    category = models.CharField(max_length=60, blank=True, null=True)
    items = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    sales = models.IntegerField(default='0', blank=True, null=True)

    def __str__(self):
	    return self.items

class Sales(models.Model):
    id_sale = models.CharField(max_length=60, blank=True, null=False)
    category = models.CharField(max_length=60, blank=True, null=True)
    items = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    date = models.DateField(blank=True, null=True)


    def __str__(self):
	    return self.items
