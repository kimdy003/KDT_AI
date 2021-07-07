from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def eda(request):
    return render(request, 'My_EDA.html')