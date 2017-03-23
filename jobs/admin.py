from django.contrib import admin
from .models import JobCategory,Job,Profile


admin.site.register(JobCategory)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','keyskills']


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('position','jobcategory',),}

admin.site.register(Job,JobAdmin)
admin.site.register(Profile, ProfileAdmin)



# Register your models here.
