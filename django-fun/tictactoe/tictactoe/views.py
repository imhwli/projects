from django.http import HttpResponse 

def welcome(request):
    return HttpResponse("<p>Hello me</p>")