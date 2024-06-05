from django import forms
from blog.models import Post

"""
Formulários para o aplicativo 'blog'.

Este módulo contém os formulários utilizados no aplicativo 'blog',
incluindo a definição do formulário para o modelo `Post`.
"""

class PostForm(forms.ModelForm):
    """
    Formulário para o modelo `Post`.

    Este formulário utiliza o modelo `Post` e define os campos que 
    serão exibidos no formulário, permitindo a criação e edição
    de instâncias de `Post`.

    Attr:
        Meta (class): Configurações adicionais para o formulário, 
        incluindo o modelo e os campos.
    """

    class Meta:
        """
        Configurações do formulário `PostForm`.

        Define o modelo a ser utilizado (`Post`) e os campos 
        que estarão presentes no formulário.
        """
        
        model = Post
        fields = ('title', 'text',)