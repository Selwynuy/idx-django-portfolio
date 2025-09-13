from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.SinglePageView.as_view(), name='home'),
    path('contact/ajax/', views.contact_ajax, name='contact_ajax'),
    # Keep old URLs for backward compatibility
    path('about/', views.AboutView.as_view(), name='about'),
]
