from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories']=category_list
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")


def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")



