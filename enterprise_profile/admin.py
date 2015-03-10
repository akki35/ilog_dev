from django.contrib import admin
from enterprise_profile.models import EnterpriseProfile

class EnterpriseProfileAdmin(admin.ModelAdmin):
    list_display = ['enterprise', 'address', 'contact', 'about', 'website', 'image']

admin.site.register(EnterpriseProfile, EnterpriseProfileAdmin)

# Register your models here.
