from django.contrib import admin
from .models import Profile, Skill, Experience, Project, ProjectImage, ProjectFeature, ContactMessage


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


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'caption', 'order']


class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1
    fields = ['title', 'description', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'is_featured', 'is_published', 'created_at', 'order']
    list_filter = ['project_type', 'is_featured', 'is_published', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['is_featured', 'is_published', 'order']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProjectImageInline, ProjectFeatureInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'long_description', 'project_type')
        }),
        ('Technologies & Links', {
            'fields': ('technologies', 'github_url', 'live_url', 'demo_url')
        }),
        ('Media & Settings', {
            'fields': ('featured_image', 'is_featured', 'is_published', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption', 'order']
    list_filter = ['project']
    list_editable = ['order']
    ordering = ['project', 'order']


@admin.register(ProjectFeature)
class ProjectFeatureAdmin(admin.ModelAdmin):
    list_display = ['project', 'title', 'order']
    list_filter = ['project']
    list_editable = ['order']
    ordering = ['project', 'order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Status & Timestamps', {
            'fields': ('status', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['name', 'email', 'subject', 'message']
        return self.readonly_fields