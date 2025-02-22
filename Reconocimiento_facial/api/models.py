from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagenes/', default='default.jpg')
    semestre = models.CharField(max_length=100, null=True)
    carrera = models.CharField(max_length=100, null=True)
    cedula = models.CharField(max_length=10, null=True)
    matricula = models.CharField(max_length=100, default="SIN_MATRICULA")
    telefono = models.CharField(max_length=10, null=True)
    
    
    
    def __str__(self):
        return f'{self.id_usuario} {self.nombre} {self.correo} {self.contrasena} {self.image} {self.semestre} {self.carrera} {self.cedula} {self.matricula} {self.telefono}'

    class Meta:
        db_table = 'Usuarios'