from django.shortcuts import render, redirect
from .models import Stock, Sales
from .forms import CreateItem, UpdateItem, SellItem
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import date
from django.http import HttpResponse

# Create your views here.

# Home view
def home_view(request, *args, **kwargs):
    context = {}
    user = request.user
    title = 'Welcome to stock management page'
    message = ''
    if user.is_authenticated:
        message = 'You are authenticated !'
    context = {
    "title": title,
    "message": message,
    }
    return render(request, "home.html",context)

#View to list items
@api_view(['POST', 'GET'])
#@permission_classes((IsAuthenticated,))
def list_items(request):
    title = 'List of Items'
    query = Stock.objects.all()
    context = {
		"title": title,
		"query": query,
	}
    return render(request, "list_items.html", context)

#View to add an item to db
@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def add_items(request):
    form = CreateItem(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_items')

    context = {
    	"form": form,
    	"title": "Add an Item",
    }
    return render(request, "add_items.html", context)

# View to delete an item from db
@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def delete_items(request, id):
	queryset = Stock.objects.get(id=id)
	if request.method == 'POST':
		queryset.delete()
		return redirect('list_items')
	return render(request, 'delete_items.html')

# View to update an item
@api_view(['POST', 'GET'])
#@permission_classes((IsAuthenticated,))
def update_items(request, id):
    queryset = Stock.objects.get(id=id)
    form = UpdateItem(instance=queryset)
    if request.method == 'POST':
        form = UpdateItem(request.POST, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantity += int(request.POST['receive_quantity'])
            instance.receive_quantity = 0
            instance.save()
            form.save()
            return redirect('list_items')

    context = {
        'form':form
    }
    return render(request, 'add_items.html', context)

# View to sell an item and send notification if quantity <= 5
@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def sell_items(request, id):
    queryset = Stock.objects.get(id=id)
    form = SellItem(instance=queryset)
    if request.method == 'POST':
        form = SellItem(request.POST, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.quantity < int(request.POST['nb_sells']):
                return HttpResponse('Error : stock is insufficient')

            instance.quantity -= int(request.POST['nb_sells'])
            if instance.quantity <= 5:
                print('Stock notification: the remaining quantity is :', instance.quantity)
            instance.sales += int(request.POST['nb_sells'])
            instance.save()
            form.save()
            sales = Sales(
                id_sale=id,
                category=request.POST['category'],
                items=request.POST['items'],
                description=request.POST['items'],
                quantity=request.POST['nb_sells'],
                date= date.today()
            )
            sales.save()

            return redirect('list_items')
    context = {
        'form':form,
        'title': 'sell item'
    }
    return render(request, 'add_items.html', context)

#View to get sales history items
@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def sales_history(request, id):
    title = 'Sales history'
    query = Sales.objects.filter(id_sale=id)
    context = {
		"title": title,
		"query": query,
	}
    return render(request, "sales_history.html", context)