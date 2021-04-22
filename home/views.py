from django.shortcuts import render
from products import models
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    home = models.Item.objects.all()
    paginator = Paginator(home , 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request , 'home/index.html',{
        'home':page_obj
    })