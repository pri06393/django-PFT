from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from finance.forms import RegistrationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, "finance/registration.html")
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Dashboard')
        return render(request, "finance/registration.html", {'form':form })

# class LoginView(View):
#     def get(self, request, *args, **kwargs):
#         form = LoginForm()
       
#         return render(request, "finance/login.html", {'form':form })
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard')
#         return render(request, "finance/login.html", {'form':form })


# def dashboard(request):
#     return render(request, 'finance/dashboard.html')
class DashboardView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        return render(request, "finance/dashboard.html")
    
# class Home(View):
#     def get(self,request,*args,**kwargs):
#         return render(request, "finance/login.html")



# def test(request):
#     return HttpResponse("test")