from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .tasks import send_email


class IndexView(TemplateView):
    template_name ='index.html'


class SentMailView(View):
    def get(self,request):
        send_email.delay()
        return HttpResponse('Sent Email successfully')
        
