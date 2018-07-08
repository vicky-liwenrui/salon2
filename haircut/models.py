from django.db import models

class Order(models.Model):
	barber_name = models.CharField(max_length=180, null=True, blank=True)
	time = models.CharField(max_length=180, null=True, blank=True)
	customer_name = models.CharField(max_length=180, null=True, blank=True)
