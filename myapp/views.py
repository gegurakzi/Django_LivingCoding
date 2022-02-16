from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def index(req):

    return HttpResponse('Welcome!')

def create(req):

    return HttpResponse('create')

def read(req, id):

    return HttpResponse('read'+str(id))