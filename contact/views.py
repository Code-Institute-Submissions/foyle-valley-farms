from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from django.http import HttpResponse
from .forms import ContactForm
from checkout.models import Order
from profiles.models import UserProfile

import os




def contact(request):
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    
                    f"Message from {full_name}, <{user_email}>", 
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('contact_thankyou')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            contact_form = ContactForm(initial={
                'email': profile.user.email,
                })
        else:
            contact_form = ContactForm()

    context = {
        'contact_form': contact_form,        
    }

    return render(request, 'contact/contact.html', context)

def contact_thankyou(request):
    """
    A view to return contact_thankyou page in order \
        to inform user that the message was succseddfully sent
    """
    return render(request, 'contact/contact_thankyou.html')