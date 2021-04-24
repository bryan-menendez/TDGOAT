from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from lists.models import Item


def index(request):    
    if request.method == "POST":    
        Item.objects.create(text=request.POST['new_item'])
        return redirect("/lists/the-one-and-only-forever-and-ever-till-the-end-of-time")

    return render(request, 'lists/index.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})
