from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    html="""DataFlair Django Tutorial<html><body><h1> Hello World DataFlair Dango tutorials</h1></body></html>"""
    return HttpResponse(html)
