from django import forms
from .models import Stock

# Form to create / add a new item to the stock

# Form To create an item 
class CreateItem(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'items', 'description', 'quantity']

# Form To update an item 

class UpdateItem(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'items', 'description', 'quantity', 'receive_quantity']


class SellItem(forms.ModelForm):

    nb_sells = forms.CharField(max_length=10)

    class Meta:
        model = Stock
        fields = ['category', 'items', 'description', 'quantity', 'nb_sells']

    

