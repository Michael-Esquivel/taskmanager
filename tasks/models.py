from django.db import models
from django.contrib.auth.models import User

class taskM(models.Model):
    title = models.CharField(max_length=20, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add = True)
    dateComplete = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.title +' - '+ self.user.username

