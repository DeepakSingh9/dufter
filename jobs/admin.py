from django.contrib import admin
from .models import JobCategory,Job,Profile,Job_Application




class JobCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','date_of_birth','keyskills']


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('position','jobcategory',),}
    list_display = ['position','jobcategory','organisation']


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['profile','job_applied']

admin.site.register(Job,JobAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(JobCategory,JobCategoryAdmin)
admin.site.register(Job_Application,JobApplicationAdmin)



# Register your models here.
