from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Profile, Skill, Experience, Project, ContactMessage
from .forms import ContactForm


class SinglePageView(TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['skills'] = Skill.objects.all()
        context['experience'] = Experience.objects.all()
        context['featured_projects'] = Project.objects.filter(
            is_published=True, 
            is_featured=True
        ).order_by('order', '-created_at')[:3]
        context['projects'] = Project.objects.filter(
            is_published=True
        ).order_by('order', '-created_at')
        return context


# AJAX contact form handler
def contact_ajax(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification
            try:
                send_mail(
                    f'New Contact Form Submission: {contact_message.subject}',
                    f'Name: {contact_message.name}\n'
                    f'Email: {contact_message.email}\n'
                    f'Subject: {contact_message.subject}\n'
                    f'Message:\n{contact_message.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            return JsonResponse({'success': True, 'message': 'Thank you for your message! I\'ll get back to you soon.'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})


# Keep the old views for backward compatibility if needed
class HomeView(TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['featured_skills'] = Skill.objects.filter(is_featured=True)[:6]
        context['recent_experience'] = Experience.objects.filter(type='work')[:3]
        return context


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['skills'] = Skill.objects.all()
        context['experience'] = Experience.objects.all()
        return context