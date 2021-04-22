from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Item , OrderItem , Order
from django.urls import reverse
# Create your views here


def products(request):
    products = Item.objects.all()
    return render(request,'products/men.html' , {"products":products})


def products_details(request , slug):
    products_details = Item.objects.get(slug=slug)
    context = {'products_details':products_details}
    return render(request ,'products/prod.html' , context)


def our(request):
    return render(request,'products/our.html')




def add_to_cart(request , slug):
    item = Item.objects.get(slug= slug)
    order_item = OrderItem.objects.create(item=item , user=request.user)
    order_qs = Order.objects.filter(user=request.user , ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order in the order
        if order.item.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    #else:
        #order = order.objects.create(user=request.user)
       # order.items.add(order_item)
    return HttpResponseRedirect(reverse('products:products'))
