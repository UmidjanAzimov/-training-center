from django.urls import path
from .views import *
from pages import views 

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact_us/', views.contact_us, name='contact'),
    path('about/', About.as_view(), name='about'),
    path('categories/', Categories.as_view(), name='categories'),
    path('blog/', Blog.as_view(), name='blog')
]