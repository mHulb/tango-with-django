from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, cookie, candy, cupcake! Yes...!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse('''Rango says: "This is the about page!"
        <a href="/rango">Go back</a>''')
