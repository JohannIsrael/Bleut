from django.db import models
from django.contrib.auth.models import User


class SignupUser(models.Model):
    id_user_django = models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)
    cel = models.CharField(max_length=10)
    imagen = models.ImageField(default='static/assets/user/25profile_default.png',upload_to='static/assets/user/', null=True)
    ciudad = models.CharField(max_length=100, null=True, blank=False)
    calle = models.CharField(max_length=100, null=True, blank=False)
    num = models.IntegerField(null=True, blank=False) 
    Es_trabajador = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{}".format(self.id_user_django)
    
    def delete(self, usign=None, kee_parents=False):

        if self.imagen.name != 'static/assets/user/25profile_default.png':
            self.imagen.storage.delete(self.imagen.name)
        super().delete()