import os

import logging

from dotenv import load_dotenv
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserProfile

load_dotenv()

logger = logging.getLogger(__name__)


@shared_task
def send_welcome_email(user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user=user)

        if user_profile.welcome_email_sent:
            return

        subject = f'Welcome to Our Website, {user_profile.user.username}!'
        message = f'Thank you for registering. Your registration date is {user_profile.registration_date}.'
        from_email = os.environ.get('EMAIL_HOST_USER')
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)

        user_profile.welcome_email_sent = True
        user_profile.save()

    except Exception as e:
        logger.error(f"Error sending welcome email: {str(e)}")
