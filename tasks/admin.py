from django.contrib import admin
from .models import Task 

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",) # muestra cuando fue creado
admin.site.register(Task, TaskAdmin )