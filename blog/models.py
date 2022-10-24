from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    autor = models.CharField(null=True, max_length=255)
    titulo = models.CharField(null=True, max_length=255)
    subtitulo = models.CharField(null=True, max_length=255)
    resumo = RichTextField(blank=True, null=True)
    conteudo = RichTextUploadingField(null=True)
    imagem_capa = models.ImageField(null=True, blank=True, upload_to='static/blog/')
    data_publicacao = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.titulo