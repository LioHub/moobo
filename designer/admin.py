from django.contrib import admin
from designer.models import User
from designer.models import Project
from designer.models import Statement

# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Statement)