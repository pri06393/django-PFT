from django.contrib import admin
from django.urls import path
from finance.views import  RegisterView, DashboardView
from finance import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('', DashboardView.as_view(),name = 'Dashboard'),
    
    #path('login/', auth)
    #path('register/dashboard',views.dashboard)
    #path('login/', LoginView.as_view(), name = 'home'),
    # path('', views.Home)
]