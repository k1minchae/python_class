from django.shortcuts import render, redirect
from .models import Restaurant, Category, Menu
from .forms import RestaurantForm, MenuForm, MenuUpdateForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    category = Category.objects.all()
    context = {
        'restaurants':restaurants,
        'category': category,
    }
    return render(request, 'restaurants/index.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurants:detail', restaurant.pk)
    form = RestaurantForm()
    context = {
        'form': form,
    }
    return render(request, 'restaurants/create.html', context)

def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk = restaurant_pk)
    category = Category.objects.get(pk=restaurant.catrgory_id)
    form = MenuForm()
    menu = Menu.objects.filter(restaurant = restaurant.pk)
    context = {
        'form': form,
        'category':category,
        'restaurant': restaurant,
        'menu': menu,
    }
    return render(request, 'restaurants/detail.html', context)

def create_menu(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    menu_form = MenuForm(request.POST)
    if menu_form.is_valid():
        menu = menu_form.save(commit = False)
        menu.restaurant = restaurant
        menu.save()
        return redirect('restaurants:detail', restaurant.pk)
    context = {
        'menu_form': menu_form,
        'restaurant': restaurant,
        
    }
    return render(request, 'restaurants:detail', context)

def update_menu(request, restaurant_pk, menu_pk):
    restaurant = Restaurant.objects.get(pk = restaurant_pk)
    menu = Menu.objects.get(pk = menu_pk)
    if request.method == 'POST':
        menu_update_form = MenuUpdateForm(request.POST, instance = menu)
        if menu_update_form.is_valid():
            menu = menu_update_form.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        menu_update_form = MenuUpdateForm()
    context = {
        'menu_update_form': menu_update_form,
    }
    return render(request, 'restaurants/update.html', context)