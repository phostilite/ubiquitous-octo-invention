from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('unleash_data/', views.unleash_data, name='unleash_data'),
    path('get_started/', views.get_started, name='get_started'),

    path('submit-form/', views.submit_form, name='submit_form'),
    path('get-started-submit/', views.get_started_submit, name='get_started_submit'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),

    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    
]
