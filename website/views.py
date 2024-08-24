from django.shortcuts import render

def landing_page(request):
    return render(request, 'website/landing_page.html')