from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context=context)

def wine_list(request):
    context = {}
    return render(request, 'wine_list.html', context=context)