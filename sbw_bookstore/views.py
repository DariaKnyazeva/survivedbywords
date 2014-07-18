from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def book(request, title):

    template = get_template('book_details.html')
    html = template.render(Context({'title': title}))

    return HttpResponse(html)
        
def books(request, title=None):
    return HttpResponse("All Books")

def authors(request, name):
    return HttpResponse("Authors")
