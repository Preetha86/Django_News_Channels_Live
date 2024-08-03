from django.shortcuts import render

# Create your views here.
def Demo(request):
    return render(request,'Demo.html')