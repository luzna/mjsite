from django.shortcuts import render

# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from main.models import *
import os
from main.forms import ContactForm
from django.core.mail import send_mail

def index(request):
    #post = Post.objects.all().order_by('-posted_date')
    return render_to_response('index.html',
            {},
            context_instance=RequestContext(request))

def kontakt(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            user = request.POST.get('user', '')
            contact_email = request.POST.get('contact_email', '')
            content = request.POST.get('content', '')
            title = request.POST.get('title','')

            content = "from: " + user+"<"+contact_email+">\n"\
                    + content

            send_mail(title, content, contact_email,['wluzna@gmail.com'])

            return redirect('/odp')

    return render_to_response( 'kontakt.html',
        {'form' : form_class},
            context_instance=RequestContext(request))

def koncerty(request):
    concerts = Concert.objects.all().order_by('-date_time')
    return render_to_response('koncerty.html',
            {'concerts' : concerts},
            context_instance=RequestContext(request))

def bio(request):
	return render_to_response('bio.html',
            {},
            context_instance=RequestContext(request))

def mainpage(request):
	return render_to_response('news.html',
            {},
            context_instance=RequestContext(request))

def galeria(request):
    mypath = '/home/manfredi/django/manfrediandjohnson/main/media/photos/new'
    files = [f for f in os.listdir(mypath)]
    return render_to_response('galeria.html',
            {'files' : files },
            context_instance=RequestContext(request))

def media(request):
    return render_to_response('media.html',
            {},
            context_instance=RequestContext(request))

def przyjaciele(request):
    return render_to_response('przyjaciele.html',
            {},
            context_instance=RequestContext(request))

def nagrody(request):
    return render_to_response('nagrody.html',
            {},
            context_instance=RequestContext(request))

def odp(request):
    return render_to_response('odp.html',
            {},
            context_instance=RequestContext(request))

def guestbook(request):
    return render_to_response('guestbook.html',
            {},
            context_instance=RequestContext(request))