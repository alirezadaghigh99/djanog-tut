from django.core.exceptions import ValidationError
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Login_Form, Register_Form
from .models import User as User
from django.contrib.auth.models import User as Save_User
from django.contrib.auth import authenticate, login

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
            data = form.cleaned_data

            user_name = data["user_name"]
            password = data["password"]
            user = authenticate(username=user_name, password=password)
            print(user, "sdflklksjdf")
            if user is not None:
                login(request,  user)
                return HttpResponseRedirect("/success")


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
            data = form.cleaned_data
            user_name = data["user_name"]
            password = data["password1"]
            name = data["name"]
            email= data['email']
            new_user = User(user_name=user_name, name=name, email= email, password= password)
            new_user.save()
            user = Save_User.objects.create_user(username=user_name, password= password, first_name= name)
            user.save()
            
            return HttpResponseRedirect('/login/')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})

class SuccessLogin(View):
    template_name = 'success.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    