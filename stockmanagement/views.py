from django.shortcuts import render, redirect
from .models import Stock
from .forms import CreateItem, UpdateItem
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def list_items(request):
    title = 'List of Items'
    query = Stock.objects.all()
    context = {
		"title": title,
		"query": query,
	}
    return render(request, "list_items.html", context)

#View to add an item to db
@api_view(['POST'])
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
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def delete_items(request, id):
	queryset = Stock.objects.get(id=id)
	if request.method == 'POST':
		queryset.delete()
		return redirect('list_items')
	return render(request, 'delete_items.html')

# View to update an item
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def update_items(request, id):
    queryset = Stock.objects.get(id=id)
    form = UpdateItem(instance=queryset)
    if request.method == 'POST':
        form = Stock(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')

    context = {
        'form':form
    }
    return render(request, 'add_items.html', context)