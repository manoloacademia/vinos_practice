from django.shortcuts import render
from .models import Wine, Winery, Brand

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context=context)

def wine_list(request):
    wine_list = Wine.objects.all()
    context = {'wine_list': wine_list}
    return render(request, 'wine_list.html', context=context)