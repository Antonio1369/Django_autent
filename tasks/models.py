from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)# por defecto esta vacio
    created = models.DateTimeField(auto_now_add=True)# la fecha y la hora esta por defecto
    datecompleted =models.DateTimeField(null=True)#campo vacio inicialmente
    important = models.BooleanField(default=False)#por defecto todaas las tareas no son importantes
    user = models.ForeignKey(User,on_delete=models.CASCADE)#es la realcion entre caracteres, CASCADE si uno se elimina se borra toda la tabla

    def __str__(self):
        return self.title + 'por ' + self.user.username
