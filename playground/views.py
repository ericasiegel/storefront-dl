from django.shortcuts import render

# Create your views here.
# Views takes a request that returns a response



def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Erica'})