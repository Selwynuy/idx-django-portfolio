from django.contrib import admin
from .models import Profile, Skill, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'title', 'email', 'location']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('user', 'first_name', 'last_name', 'title', 'bio')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Media', {
            'fields': ('profile_image', 'resume')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url', 'website_url')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    search_fields = ['name']
    list_editable = ['proficiency', 'is_featured', 'order']
    ordering = ['order', 'name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'type', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['type', 'is_current', 'start_date']
    search_fields = ['title', 'company', 'description']
    list_editable = ['is_current', 'order']
    ordering = ['-start_date', 'order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'location', 'type')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Content', {
            'fields': ('description', 'order')
        }),
    )