from django.shortcuts import render

# Create your views here.
#function based views

def test_view(request):
    return render(request, 'pages/test.html') 

def about_view(request):
    return render(request, 'pages/about.html')

