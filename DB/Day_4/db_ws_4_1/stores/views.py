from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import CreateStoreForm, CreateProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores':stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    products = Product.objects.filter(store=store.pk)
    form = CreateProductForm()
    context = {
        'products': products,
        'store':store,
        'form': form,
    }
    return render(request, 'stores/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateStoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
    else:
        form = CreateStoreForm()
    context = {
        'form':form,
    }
    return render(request, 'stores/create.html', context)

def add_product(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    form = CreateProductForm(request.POST)
    if form.is_valid() and request.user == store.user:
        product = form.save(commit=False)
        product.store = store
        product.user = store.user
        product.save()
        return redirect('stores:detail', store.pk)
    return render(request, 'stores/detail.html', store_pk)

def delete_product(request, store_pk, product_pk):
    product = Product.objects.get(pk = product_pk)
    if request.user == product.user:
        product.delete()
    return redirect('stores:detail', store_pk)