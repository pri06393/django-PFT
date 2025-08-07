from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from finance.forms import RegistrationForm, TransactionForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from django.db.models import Sum


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

# class DashboardView(LoginRequiredMixin,View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "finance/dashboard.html")
    
class TransactionCreationView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, "finance/transaction.html", {'form':form })
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit = False)
            transaction.user = request.user
            transaction.save()
            return redirect('Dashboard')
        return render(request, "finance/transaction.html", {'form':form })
    
class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        Transactions = Transaction.objects.all()
        return render(request, "finance/transaction_list.html", {'Transactions': Transactions})
    

# def updateTransaction(request,pk):
#     transaction = get_object_or_404(Transaction, id = pk)
#    # Transactions = TransactionForm(instance=order)
#     if request.method =='POST':
#         form = TransactionForm(request.POST, instance = transaction)
#         if form.is_valid():
#             form.save()
#             return redirect('transaction_list')
#         else:
#             form = TransactionForm(instance=transaction)

#     # context = {'Transactions':Transactions}
#     return render(request, "finance/transaction.html",{'form':form})

def updateTransaction(request, pk):
    transaction = get_object_or_404(Transaction, id=pk)  # this avoids None
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')  # make sure this name exists in urls
    else:
        form = TransactionForm(instance=transaction)
    return render(request, "finance/transaction.html", {'form': form})








def deleteTransaction(request,pk):
    transaction = get_object_or_404(Transaction, id = pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'finance/deleteTransaction.html',{'item':transaction})


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user=request.user).order_by('-date')
        total_income = transactions.filter(transaction_type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = transactions.filter(transaction_type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expenses
        recent_transactions = transactions[:5]  # Show 5 recent
        context = {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'balance': balance,
            'recent_transactions': recent_transactions,
        }
        return render(request, "finance/dashboard.html", context)