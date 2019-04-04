from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'homepage.html')

def predict(request,slug):
    data = {}
    return JsonResponse(data)