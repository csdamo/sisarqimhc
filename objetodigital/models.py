from django.db import models

from documento.models import Documento

        
class ObjetoDigital(models.Model):

    codigo = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    documento = models.ForeignKey(Documento, on_delete=models.PROTECT, related_name='objeto_digital')
    arquivo = models.FileField(upload_to='documentos/')
    
    TIPO_QUALIDADE = (
        ('1', 'Baixa'),
        ('2', 'Media'),
        ('3', 'Alta'),
    )
    
    qualidade = models.CharField(
	    max_length=1,
	    choices=TIPO_QUALIDADE,
	    default='1',
	)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Arquivo: {self.codigo} - Documento: {self.documento}"
    
    class Meta:
        db_table = "objetodigital"
        verbose_name_plural = "ObjetosDigitais"
        ordering = ['codigo']
        