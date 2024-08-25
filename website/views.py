from django.shortcuts import render

def landing_page(request):
    return render(request, 'website/landing_page.html')

def about(request):
    return render(request, 'website/about.html')

def services(request):
    return render(request, 'website/services.html')

def contact(request):
    return render(request, 'website/contact.html')

def unleash_data(request):
    return render(request, 'website/unleash_data.html')

def get_started(request):
    return render(request, 'website/get_started.html')