from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail
# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
class Categories(TemplateView):
    template_name = 'categories.html'
    
class Blog(TemplateView):
    template_name = 'blog.html'
    
def contact_us(request):
    if request.method == "POST": 
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        text = request.POST.get('text')
        contact.name=name
        contact.email=email
        contact.phone_number=phone_number
        contact.message=text
        contact.save()
        return render(request, 'contact.html', {'name': name})
    return render(request, 'contact.html', {})    
        
        
    #     send_mail(
    #         'Message from' + name,
    #         'Email of sender' + email,
    #         'Phone number of sender' + phone_number,
    #         ['umidjanmrazimov02@gmail.com']
    #     )
        
    #     return render(request, 'contact.html', {'name': name})
    # else:
    #     return render(request, 'contact.html', {})