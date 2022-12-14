from django.shortcuts import redirect, render
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

def brand_detail(request):
    brand_list = Brand.objects.all()
    context = {"brand_list": brand_list}
    return render(request, 'brand_detail.html', context=context)

def winery(request):
    wineries = Winery.objects.all()
    context = {"wineries": wineries}
    return render(request, 'winery.html', context=context)

def search_products(request):
    search = request.GET['search']
    wines = Wine.objects.filter(name__icontains=search)  #Trae los que cumplan la condicion
    context = {'wines':wines}
    return render(request, 'search.html', context=context)