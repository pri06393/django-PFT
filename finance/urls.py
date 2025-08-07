from django.contrib import admin
from django.urls import path
from finance.views import  RegisterView, DashboardView, TransactionCreationView, TransactionListView, updateTransaction, deleteTransaction, export_transactions_csv
from finance import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('', DashboardView.as_view(),name = 'Dashboard'),
    path('transaction/add/', TransactionCreationView.as_view(),name = 'Transaction_add'),
    path('transaction/', TransactionListView.as_view(),name = 'transaction_list'),
    path('transaction/update/<str:pk>', views.updateTransaction,name = 'update_list'),
    path('transaction/delete/<str:pk>', views.deleteTransaction,name = 'delete_list'),
    path('transaction/download/', views.export_transactions_csv,name = 'download_csv'),


    
    
   
]