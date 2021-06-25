from django.contrib import admin
from .models import Stock
from .forms import CreateItem
# Register your models here.

class AdminStock(admin.ModelAdmin):

   list_display = ['category', 'items', 'description', 'quantity']
   form = CreateItem
   list_filter = ['category']
   search_fields = ['category', 'items']

admin.site.register(Stock, AdminStock)
