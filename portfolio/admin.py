from django.contrib import admin


from .models import Profile, Work, Education, Skills, Certificate, Project

# Register your models here.

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Certificate)
admin.site.register(Project)