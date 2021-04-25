from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from lists.models import Item, List


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['new_item'], list=list_)
    return redirect(f'/lists/{list_.id}')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['new_item'], list=list_)
    return redirect(f"/lists/{list_.id}")


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': list_})


def index(request):
    return render(request, 'lists/index.html')


