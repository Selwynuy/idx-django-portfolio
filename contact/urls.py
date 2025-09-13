from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
    path('ajax/', views.contact_ajax, name='contact_ajax'),
]
