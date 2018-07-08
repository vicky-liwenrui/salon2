from django.shortcuts import render
from . models import Order
def home_page(request):
	orders = Order.objects.all()
	if request.method == 'POST':
		our_barber_name = request.POST.get('barber_name')
		our_time = request.POST.get('time')
		our_customer_name = request.POST.get('customer_name')
		order_obj = Order.objects.create(
			barber_name=our_barber_name,
			time=our_time,
			customer_name=our_customer_name
		)
		orders = Order.objects.all()
		return render(request, 'haircut/home_page.html', {'orders':orders,})

	return render(request, 'haircut/home_page.html', {'orders':orders,})