from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'roll_number', 'program', 'gpa', 'status')
    list_filter = ('program', 'status', 'admission_date')
    search_fields = ('full_name', 'roll_number')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('full_name', 'roll_number', 'program', 'profile_pic')
        }),
        ('Academic Information', {
            'fields': ('gpa', 'admission_date', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Student, StudentAdmin)