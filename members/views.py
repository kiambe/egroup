from django.shortcuts import render,reverse,redirect,resolve_url

# from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.views.generic import CreateView

#from .forms import SignupForm,LoginForm,UpdateDefaultProfile,UpdateCustomProfile
from django.contrib import messages
#from customers.models import Customer
#from orders.models import Order
#from registers.models import Profile
#from products.models import Product,HistConf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
#from .decorators import unauthenticated_user, allowed_users, admin_only
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
#from registers.filters import CustomerFilter

# from datetime import datetime
# from django.utils import timezone
from datetime import datetime, timedelta


# from django.contrib.auth.mixins import LoginRequiredMixin

# @allowed_users(allowed_roles=['admin'])
#@login_required(login_url='/user/login/')
# @admin_only
def dashboard(request):
	# customer = Customer.objects.get(pk=cid)
	"""customers=Customer.objects.all()
	total_customers=customers.count()
	orders=Order.objects.all()

	total_orders=orders.count()
	products = Product.objects.all()
	total_products = products.count()	
	pending=orders.filter(status='Pending').count()#filter la choose(search)  garxa and all pending lai count garxa
	delivered=orders.filter(status="Delivered").count()
 
 
	myFilter = CustomerFilter(request.GET, queryset=customers)
	customers = myFilter.qs #in jinja this customers goes

	# today_date = datetime.today()#filter every day order product for daily expenses	

	# today_customers = customers.filter(date_created__year = today_date.year,date_created__month = today_date.month,
	#                                 date_created__day = today_date.day).count()
	
	today_customers = customers.filter(date_created__gte = datetime.now() - timedelta(days=1)).count()#details of last 24 hours#b4 i also get same output using above line but now not so use this concept
	# today_order = orders.filter(created_at__year = today_date.year,created_at__month = today_date.month,created_at__day = today_date.day)
	today_order = orders.filter(created_at__gte = datetime.now() - timedelta(days=1))#A timedelta object represents a duration, the difference between two dates or times.

	order_total_price=0.00
 
	for order in today_order:
		per_total_price = float(order.product.price) * order.quantity
		
		order_total_price += per_total_price
  
	print(order_total_price)
	# customer = Customer.objects.get(pk=cid) #but i need pk = cid(update)
	# particular_customer_price=0.00
	# for order in customer.order_set.all():
	# 	per_total_price = float(order.product.price) * order.quantity
	# 	particular_customer_price += per_total_price """
	context={
			"""'customers':customers,'orders_total_price':order_total_price,'total_orders':total_orders,
   			'myFilter':myFilter,'today_customers':today_customers,'current_data':datetime.now(),
			'orders_pending':pending,'orders_delivered':delivered,'total_products':total_products,'total_customers':total_customers"""
			"data":1
			}
	
	return render(request,'index.html',context)

