from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('sent_mail',SentMailView.as_view(),name='sent_mail')
]