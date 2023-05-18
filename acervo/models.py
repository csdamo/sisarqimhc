from django.db import models


class Acervo(models.Model):

    codigo = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=255, unique=True)
    sigla = models.CharField(max_length=30, unique=True)
    descricao = models.TextField()
    info_adicionais = models.TextField(blank=True, null=True)
    ordem_exibicao = models.PositiveSmallIntegerField()
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Acervo {self.sigla}"

    class Meta:
        db_table = "acervo"
        verbose_name_plural = "Acervos"
        ordering = ['sigla']
        