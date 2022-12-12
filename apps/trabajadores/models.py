from django.db import models
from ..authentication.models import User
# Create your models here.

tipo_licencias = [('1','Pro'),('2','Plus'),('3','Normal')]

class SolicitudTrabajador(models.Model):
    id = models.BigAutoField(primary_key=True)
    curriculum = models.FileField(upload_to='static/assets/cv/', null=False, blank=True)     

    def __str__(self) -> str:
        return "{}".format(self.id)    

    class Meta: 
        db_table = "Solicitudes Trabajadores"

    # def delete(self, usign=None, kee_parents=False):
    #     self.curriculum.storage.delete(self.curriculum.name)
    #     super().delete()

class Licencia(models.Model):
    id = models.BigAutoField(primary_key=True)   
    clave = models.CharField(max_length=100, null=True)
    tipo = models.CharField(choices=tipo_licencias, null=False, default=3, max_length=20)
    duracion = models.DurationField()
    price = models.FloatField(null=False)

    def __str__(self) -> str:
        return "{}".format(self.id) 

    class Meta: 
        db_table = "Licencias"

class SignupTrabajador(models.Model):
    id = models.BigAutoField(primary_key=True)
    RFC = models.CharField(max_length=13,  unique=True)
    id_user_trabajador = models.OneToOneField(User, on_delete=models.CASCADE)
    idlicencia = models.OneToOneField(Licencia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return " {}".format(self.id_user_trabajador)    

    class Meta: 
        db_table = "Trabajadores"
    
class Oficio_trabajador(models.Model):
    id = models.BigAutoField(primary_key=True)
    trabajador = models.ForeignKey(SignupTrabajador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100,null=True,blank=True) # Aqui agregar la libreria de edicion
    horario = models.TimeField() # aqui agregar un calendario para selecionar dias
   # price = models.FloatField()

    def __str__(self) -> str:
        return "{} ({})".format(self.id, self.trabajador) 

    class Meta: 
        db_table = "Oficios"

class Calificacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    puntaje = models.IntegerField()
    descripcion = models.CharField(max_length=100, null=True, blank=True) # Aqui agregar la libreria de edicion
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)

    def __str__(self) -> str:
        return "{} ({})".format(self.id, self.autor)

    class Meta: 
        db_table = "Calificacion"


class Comentarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True) # Aqui agregar la libreria de edicion
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)

    def __str__(self) -> str:
        return "{} ({})".format(self.id, self.autor)

    class Meta: 
        db_table = "Comentarios"


class Perfil_Oficios(models.Model):
    id = models.BigAutoField(primary_key=True)
    oficio = models.ForeignKey(Oficio_trabajador, null=False, on_delete=models.PROTECT )
    id_coment = models.ForeignKey(Comentarios, on_delete=models.CASCADE)
    id_calif = models.ForeignKey(Calificacion, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "{} ({})".format(self.id, self.oficio)

    class Meta: 
        db_table = "Perfil_Oficios"


    
