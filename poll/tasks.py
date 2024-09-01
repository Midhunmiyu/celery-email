from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sub(x,y):
    sleep(5)
    return x - y

@shared_task
def send_email():
    subject = 'New Form Submission-ZAYAN Website'
    message_body = f'Hello'
    from_email = 'fastmail@smtp-mail.noviindus.co.in'
    to_email = 'midhun@noviindus.com'
    send_mail(subject, message_body, from_email, [to_email])