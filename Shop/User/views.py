from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import Login_Form, Register_Form
# Create your views here.

class Login(View):
    
    data = {
        "user_name": "salam",
        "password" : "sss"
    }
    form = Login_Form
    template_name = 'login.html'
    initial = {"key" : "value"}
    def get(self, request, *args, **kwargs):
        form = self.form(initial= self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
                # <process form cleaned data>
            return HttpResponse('success')

        return render(request, self.template_name, {'form': form})



class Register(View):
    
    form = Register_Form
    template_name = 'register.html'
    initial = {"key" : "value"}
    def get(self, request, *args, **kwargs):
        form = self.form(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
                # <process form cleaned data>
            print(form.cleaned_data)
            return HttpResponse('success')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})
