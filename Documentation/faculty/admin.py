from django.contrib import admin
from . import models
# Register your models here.
class facultyAdmin(admin.ModelAdmin):
    list_display=('subject','sem',)

admin.site.register(models.mfrequest,facultyAdmin)