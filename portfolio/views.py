from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Profile, Skill, Experience
from projects.models import Project


class SinglePageView(TemplateView):
    template_name = 'portfolio/single_page.html'
    
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