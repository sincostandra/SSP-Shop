from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'shop_name' : 'SSP Shop',
        'name' : 'Utandra Nur Ahmad Jais (2306152443)',
        'class' : 'PBP F'
    }

    return render(request, 'main.html', context)