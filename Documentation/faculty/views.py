from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def faculty(request):
    return HttpResponse('this is faculty page')