from django.contrib import admin
from .models import JobCategory,Job,Profile

admin.site.register(Job)
admin.site.register(JobCategory)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','keyskills']


admin.site.register(Profile,ProfileAdmin)



# Register your models here.
