from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):    
    return render(request, 'lists/index.html', {
            'new_item_html' : request.POST.get('new_item', ''),
        })
