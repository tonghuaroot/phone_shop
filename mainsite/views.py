from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mainsite import models

# Create your views here.
def index(request):
    products = models.Product.objects.all()
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)