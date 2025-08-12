from django.contrib import admin
# Register your models here.
# admin.site.register(User)
# from django.contrib import admin
from finance.models import Transaction  # Import your model from the models.py file in the same app

admin.site.register(Transaction)