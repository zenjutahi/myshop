from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart 
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order 

# Create your views here.
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order, product=item['product'],
										price=item['price'], quantity=item['quantity'])
			# clear the cart
			cart.clear()
			# launch asynchronous task
			order_created.delay(order.id)
			context = {'order': order }
			return render(request, 'orders/order/created_try.html', context)
	else:
		form = OrderCreateForm()
	context = {'cart': cart,
				'form': form }
	return render(request, 'orders/order/create_try.html', context)

@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	context = {'order': order}
	return render(render, 'admin/orders/order/detail.html', context)