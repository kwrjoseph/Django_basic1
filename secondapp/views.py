from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    faq_dict = {'insert_me': "here is help"}

    return render(request, 'secondapp/help.html', context=faq_dict)



def blog(request):
    faq_dict = {'insert_me': "blog posted"}

    return render(request, 'secondapp/help.html', context=faq_dict)



