from django.contrib import admin
from .models import Project, ProjectImage, ProjectFeature


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