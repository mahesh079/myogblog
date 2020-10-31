from django.shortcuts import render
from django.http import HttpResponse

def mainindex(request):
    return render(request,"shop/mainindex.html")