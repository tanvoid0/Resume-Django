from django.contrib import admin

# Register your models here.
from portfolio.models import Project, Project_Category, Project_Feature, Project_Tag

admin.site.register(Project)
admin.site.register(Project_Category)
admin.site.register(Project_Feature)
admin.site.register(Project_Tag)