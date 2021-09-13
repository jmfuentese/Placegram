"""Platzigram views"""

import json
#Django 
from django.http import HttpResponse, JsonResponse
from datetime import date, datetime #Utilities

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {now}')

def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = sorted([int(x) for x in str(request.GET['numbers']).split(',')])
    data = {
        'status' : 'ok',
        'numbers' : numbers,
        'message' : 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=4))

def say_hi(request, name, age):
    """Return a greeting"""
    if age<12:
        message = f"Sorry {name}, you are not allowd here."
    else:
        message = f"Hello {name}! Welcome to platzigram."
    return HttpResponse(message)