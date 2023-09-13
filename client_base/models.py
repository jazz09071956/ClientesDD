from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

# Crearemos un modelo que sera comun a todas las tablas (modelos).
class TablaBase(models.Model):
  estado = models.BooleanField(default=True)
  creado =models.DateTimeField(auto_now_add=True)
  modificado =models.DateTimeField(auto_now=True)
  #creo =models.ForeignKey(User, on_delete=models.CASCADE)
  #modifico =models.IntegerField(blank=True,null=True)
# ya incluye el userforeignkey
  creo = UserForeignKey(auto_user_add=True,related_name='+')
  modifico = UserForeignKey(auto_user=True,related_name='+')

# para que no la tome en cuenta a la hora de una migracion
  class Meta:
    abstract=True

