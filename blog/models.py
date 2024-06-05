from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    """
    Modelo para representar um post no blog.

    Este modelo inclui campos para autor, título, texto, 
    data de criação e data de publicação.

    Attributes:
        author (ForeignKey): Referência ao usuário que criou o post.
        title (CharField): Título do post.
        text (TextField): Texto do post.
        created_date (DateTimeField): Data e hora de criação do post.
        published_date (DateTimeField): Data e hora de publicação do post.
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Publica o post.

        Define a data de publicação como o momento atual e salva o post.
        """

        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Retorna uma representação em string do post.

        Returns:
            str: O título do post.
        """
         
        return self.title


