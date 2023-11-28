import os

from dotenv import load_dotenv
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserProfile

load_dotenv()


@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.get(user=user)

    subject = f'Welcome to Our Website, {user_profile.user.username}!'
    message = f'Thank you for registering on our website. Your registration date is {user_profile.registration_date}.'
    from_email = os.environ.get('EMAIL_HOST_USER')
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
