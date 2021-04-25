from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from lists.models import Item, List


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['new_item'], list=list_)
    return redirect("/lists/the-one-and-only-forever-and-ever-till-the-end-of-time")


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})


def index(request):
    return render(request, 'lists/index.html')


