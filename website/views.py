# views.py
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import logging
from .utils import get_started_email_template, contact_email_template, data_revolution_email_template, subscription_email_template
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import NewsletterSubscriptionForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import NewsletterSubscription

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def landing_page(request):
    context = {
        'newsletter_form': NewsletterSubscriptionForm(),
    }
    return render(request, 'website/landing_page.html', context)

def about(request):
    context = {
        'newsletter_form': NewsletterSubscriptionForm(),
    }
    return render(request, 'website/about.html', context)   

def services(request):
    context = {
        'newsletter_form': NewsletterSubscriptionForm(),
    }
    return render(request, 'website/services.html', context)

def contact(request):
    context = {
        'newsletter_form': NewsletterSubscriptionForm(),
    }
    return render(request, 'website/contact.html', context)

def unleash_data(request):
    context = {
        'newsletter_form': NewsletterSubscriptionForm(),
    }
    return render(request, 'website/unleash_data.html', context)

def get_started(request):
    context = {
        'newsletter_form': NewsletterSubscriptionForm(),
    }
    return render(request, 'website/get_started.html', context)

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        logger.info("Received POST request for form submission")
        try:
            # Try to parse JSON data
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                # If JSON parsing fails, use request.POST
                data = request.POST

            logger.info(f"Received data: {data}")
            
            # Extract form data
            name = data.get('name')
            email = data.get('email')
            company = data.get('company')
            job_title = data.get('jobTitle')
            message = data.get('message')
            logger.info(f"Extracted form data: name={name}, email={email}, company={company}, job_title={job_title}")
            
            # Compose email message
            email_subject = f"New Data Revolution Inquiry from {company}"
            email_message = data_revolution_email_template(name, email, company, job_title, message)
            logger.info("Composed email message")
            
            # Send email
            send_mail(
                email_subject,
                '',  # Empty string for plain text version
                settings.DEFAULT_FROM_EMAIL,
                ['info@bridgesdata.ai'],
                html_message=email_message,
                fail_silently=False,
            )
            logger.info("Sent email successfully")
            
            return JsonResponse({'success': True})
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)})
    
    logger.warning("Invalid request method")
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def get_started_submit(request):
    if request.method == 'POST':
        logger.info("Received POST request for Get Started form submission")
        try:
            # Try to parse JSON data
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                # If JSON parsing fails, use request.POST
                data = request.POST

            logger.info(f"Received data: {data}")
            
            # Extract form data
            name = data.get('name')
            email = data.get('email')
            company = data.get('company')
            industry = data.get('industry')
            message = data.get('message')
            
            logger.info(f"Extracted form data: name={name}, email={email}, company={company}, industry={industry}")
            
            # Compose email message
            email_subject = f"New Get Started Inquiry from {name} at {company}"
            email_message = get_started_email_template(name, email, company, industry, message)
            
            logger.info("Composed email message")
            
            # Send email
            send_mail(
                email_subject,
                '',  # Empty string for plain text content
                settings.DEFAULT_FROM_EMAIL,
                ['info@bridgesdata.ai'],  # Replace with your admin email
                fail_silently=False,
                html_message=email_message  # Use the HTML email template
            )
            logger.info("Sent email successfully")
            
            return JsonResponse({'success': True})
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)})
    
    logger.warning("Invalid request method")
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def contact_submit(request):
    if request.method == 'POST':
        logger.info("Received POST request for contact form submission")
        try:
            # Try to parse JSON data
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                # If JSON parsing fails, use request.POST
                data = request.POST

            logger.info(f"Received data: {data}")
            
            # Extract form data
            name = data.get('name')
            email = data.get('email')
            company_url = data.get('company_url')
            subject = data.get('subject')
            message = data.get('message')
            
            logger.info(f"Extracted form data: name={name}, email={email}, company_url={company_url}, subject={subject}")
            
            # Compose email message
            email_subject = f"New Contact Form Submission: {subject}"
            email_message = contact_email_template(name, email, company_url, subject, message)
            
            logger.info("Composed email message")
            
            # Send email
            send_mail(
                email_subject,
                '',  # Empty string for plain text content
                settings.DEFAULT_FROM_EMAIL,
                ['info@bridgesdata.ai'],  # Replace with your admin email
                fail_silently=False,
                html_message=email_message  # Use the HTML email template
            )
            logger.info("Sent email successfully")
            
            return JsonResponse({'success': True})
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)})
    
    logger.warning("Invalid request method")
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if not email:
            return JsonResponse({'status': 'error', 'message': 'Email is required.'})
        
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'status': 'error', 'message': 'Invalid email address.'})
        
        try:
            subscription, created = NewsletterSubscription.objects.get_or_create(email=email)
            if created:
                # Send email notification
                email_subject = "New Newsletter Subscription"
                email_message = subscription_email_template(email)
                
                send_mail(
                    email_subject,
                    '',  # Empty string for plain text content
                    settings.DEFAULT_FROM_EMAIL,
                    ['cloudythought9@gmail.com'],  # Replace with your admin email
                    fail_silently=False,
                    html_message=email_message
                )
                
                return JsonResponse({'status': 'success', 'message': 'Successfully subscribed to the newsletter!'})
            else:
                return JsonResponse({'status': 'info', 'message': 'You are already subscribed to the newsletter.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'An error occurred. Please try again.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})