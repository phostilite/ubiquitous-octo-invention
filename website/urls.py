from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('unleash_data/', views.unleash_data, name='unleash_data'),
    path('get_started/', views.get_started, name='get_started'),
]
