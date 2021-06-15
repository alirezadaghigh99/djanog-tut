from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
  
# Create your views here.
def add_product(request):
  
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form' : form})
  