from django.db import models


class Local(models.Model):

    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Local {self.titulo}"

    class Meta:
        db_table = "Local"
        verbose_name_plural = "Locais"
        ordering = ['titulo']
