from django.contrib import admin
from . models import Order
class OrderAdmin(admin.ModelAdmin):
	list_display=('barber_name', 'time', 'customer_name')

admin.site.register(Order, OrderAdmin)