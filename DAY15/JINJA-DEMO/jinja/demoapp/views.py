
from django.shortcuts import render

def django_page(request):
    return render(request,"index.html", {"name":"Keerthana"})

def jinja_page(request):
    return render(request, "dashboard.jinja", {"name":"keerthana"})