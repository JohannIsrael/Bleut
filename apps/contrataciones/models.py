from django.db import models
from ..trabajadores.models import Perfil_Oficios
from ..clientes.models import SignupCliente
# Create your models here.
class Contrataciones(models.Model):
    id = models.BigAutoField(primary_key=True)
    servicio = models.ForeignKey(Perfil_Oficios, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(SignupCliente, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return "{} ({}) => ({})".format(self.id, self.servicio, self.cliente)

    class Meta: 
        db_table = "Contrataciones"