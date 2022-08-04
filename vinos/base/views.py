from django.shortcuts import redirect, render
from matplotlib.style import context
from .models import Wine, Winery, Brand
from .forms import WineForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context=context)

def wine_list(request):
    wine_list = Wine.objects.all()
    context = {'wine_list': wine_list}
    return render(request, 'wine_list.html', context=context)

def create_wine(request):
    if request.method == 'POST':
        form = WineForm(request.POST)
        
        if form.is_valid():
            Wine.objects.create(
                name = form.cleaned_data['name'],
                brand = form.cleaned_data['brand'],
                price = form.cleaned_data['price'],
                aged = form.cleaned_data['aged'],
                winery = form.cleaned_data['winery'])
            return redirect(wine_list)
    elif request.method == 'GET':
        form = WineForm()
        context = {'form': form}
        return render(request, 'create_wine.html', context=context)