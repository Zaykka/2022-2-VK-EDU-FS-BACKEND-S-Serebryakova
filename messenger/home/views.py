from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods



@require_http_methods(["GET"])
def index(request):
    
    return render(request, 'index.html')