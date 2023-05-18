from django.db import models
from acervo.models import Acervo


class Estrutura(models.Model):

    codigo = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=255, unique=True)
    sigla = models.CharField(max_length=30, unique=True)
    descricao = models.TextField()
    info_adicionais = models.TextField(blank=True, null=True)
    nivel = models.PositiveSmallIntegerField()
    acervo = models.ForeignKey(Acervo, on_delete=models.PROTECT)
    estrutura_nivel_superior = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Estrutura {self.titulo}"
    
    class Meta:
        db_table = "estrutura"
        verbose_name_plural = "Estruturas"
        ordering = ['sigla']
        