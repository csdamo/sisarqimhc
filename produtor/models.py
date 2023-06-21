from django.db import models


class Produtor(models.Model):

    codigo = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    info_adicionais = models.TextField(blank=True, null=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Produtor {self.titulo}"

    class Meta:
        db_table = "produtor"
        verbose_name_plural = "Produtores"
        ordering = ['titulo']
        