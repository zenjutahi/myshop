from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	query = request.GET.get("q")
	if query:
		products = products.filter(Q(name__icontains=query) | Q(category__name__icontains = query) |Q(description__icontains=query))
	
	paginator = Paginator(products, 32) # Show 16 products per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		products = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g 99999), deliver last page of results.
		products = paginator.page(paginator.num_pages)


	context = {'category':category,
				'categories':categories,
				'page_request_var': page_request_var,
				'products':products}
	return render(request, 'shop/product/list_try.html', context)

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	context = {'product':product,
				'cart_product_form':cart_product_form }
	return render(request, 'shop/product/detail_try.html', context)










