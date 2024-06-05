from django.contrib import admin
from .models import Post

"""
Configuração de administração do Django para o aplicativo 'blog'.

Este módulo registra o modelo `Post` no site de administração do Django
permitindo a gestão das instâncias do modelo através da 
interface administrativa.
"""

# Register your models here.
admin.site.register(Post)

