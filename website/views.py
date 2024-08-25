from django.shortcuts import render

def landing_page(request):
    return render(request, 'website/landing_page.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')