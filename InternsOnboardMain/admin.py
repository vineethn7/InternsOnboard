from django.contrib import admin
from .models import internshipPost

@admin.register(internshipPost)
class internshipPostAdmin(admin.ModelAdmin):
    list_display = ['company_name','description','owner','created_at']