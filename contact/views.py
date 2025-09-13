from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .forms import ContactForm


class ContactView(TemplateView):
    template_name = 'contact/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
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
                # Log the error but don't fail the form submission
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            return redirect('contact:contact')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
            return render(request, self.template_name, {'form': form})