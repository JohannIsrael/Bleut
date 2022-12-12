from django.db import models
from ..authentication.models import User

class SignupCliente(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    id_user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "{}. {}".format(self.id, self.id_user)   

    class Meta: 
        db_table = "clientes"