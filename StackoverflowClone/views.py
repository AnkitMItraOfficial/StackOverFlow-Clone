from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render (request, 'StackoverflowClone/home.html')
def test(request):
    pass
