from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Table1,Table2
def f1(request):
     obj1=Table1.objects.all()
     obj2=Table2.objects.all()
     return render(request,"index.html",{'key1':obj1,'key2':obj2})