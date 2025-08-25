import logging
from celery import shared_task
from django.db.models import Model
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

User: Model = get_user_model()

@shared_task
def notify_user_duplicate_registration(username, ip, browser, os):
    """
    Send email to user that there was an attempt to register an account with his email
    """
    now = timezone.now()
    params = {
        'username': username,
        'ip_address': ip,
        'browser': browser,
        'os': os,
        'time': now
    }
    subject = loader.get_template(f'accounts/duplicate_account_registration.txt').render()
    message = loader.get_template(f'accounts/duplicate_account_registration.html').render(context=params)

    send_mail(
        subject=subject,
        message='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[username],
        html_message=message,
        fail_silently=False
    )



@shared_task
def notify_user_ip_changed(user_id, ip, device, os, browser):
    """
    Send email to user that there was an attempt to login from a new ip address
    """
    now = timezone.now()
    user = User.objects.filter(pk=user_id).first()
    lang = user.profile.language

    params = {
        'username': user.username,
        'ip_address': ip,
        'device': device,
        'os': os,
        'browser': browser,
        'time': now
    }

    msg = loader.get_template(f'accounts/ip_changed.html').render(params).strip()
    subject = _('Nuevo inicio de sesión')
    send_mail(
        subject,
        '',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=msg,
        fail_silently=False
    )



@shared_task
def notify_failed_login(user_id):
    """
    Send email to user that there was an attempt to login with incorrect password
    """
    user = get_user_model().objects.filter(pk=user_id).first()

    params = {
        'username': user.username,
    }

    msg = loader.get_template(f'accounts/failed_login.html').render(params).strip()
    subject = _('Login fallido')
    send_mail(
        subject,
        '',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=msg,
        fail_silently=False
    )