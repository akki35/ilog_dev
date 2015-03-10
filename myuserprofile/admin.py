from django.contrib import admin
from myuserprofile.models import MyUserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['myuser', 'gender', 'job_position', 'experience',
                    'summary',  'image', ]

admin.site.register(MyUserProfile, ProfileAdmin)

# Register your models here.
