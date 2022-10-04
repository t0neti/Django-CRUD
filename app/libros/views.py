from django.shortcuts import render

# app/libros/views.py

from django.http import JsonResponse

def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)
