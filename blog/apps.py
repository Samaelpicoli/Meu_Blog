from django.apps import AppConfig

"""
Configuração do aplicativo 'blog'.

Este módulo contém a configuração da aplicação 'blog', 
que define a classe de configuração do aplicativo e suas propriedades,
como o campo padrão automático e o nome da aplicação.
"""

class BlogConfig(AppConfig):
    """
    Configuração da aplicação 'blog'.

    Esta classe contém as configurações padrão para o aplicativo 'blog',
    incluindo o campo padrão para chaves primárias 
    automáticas e o nome do aplicativo.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
