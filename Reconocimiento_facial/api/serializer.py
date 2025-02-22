from rest_framework import serializers
from .models import Usuarios


class UsuariosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuarios
        fields = ('id_usuario', 'nombre','correo','contrasena','image','semestre','carrera','cedula','matricula','telefono')
    

        
        