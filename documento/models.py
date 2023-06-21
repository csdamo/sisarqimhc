from django.db import models
from acervo.models import Acervo
from assunto.models import Assunto
from estrutura.models import Estrutura
from local.models import Local
from pessoa.models import Pessoa
from produtor.models import Produtor


class Documento(models.Model):

    codigo = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    info_adicionais = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    
    GENERO_DOCUMENTAL = (
        ('1', 'Textrual'),
        ('2', 'Iconográfico'),
        ('3', 'Audiovisual'),
        ('4', 'Fonográfico'),
        ('5', 'Cartográfico'),
        ('6', '3D'),
        ('7', 'Multimeios')
    )
    
    genero_documental = models.CharField(
	    max_length=1,
	    choices=GENERO_DOCUMENTAL,
	    default='1',
	)
    
    TIPO_PERMISSAO = (
        ('1', 'Restrição total'),
        ('2', 'Exige autorização para visualização'),
        ('3', 'Livre para visualização, restrito para download'),
        ('4', 'Livre total')
    )
    
    nivel_permissao = models.CharField(
	    max_length=1,
	    choices=TIPO_PERMISSAO,
	    default='1',
	)
    
    acervo = models.ForeignKey(Acervo, on_delete=models.PROTECT, related_name='acervo')
    estrutura = models.ForeignKey(Estrutura, on_delete=models.PROTECT, null=True, blank=True, related_name='documento')
    local = models.ForeignKey(Local, on_delete=models.PROTECT, null=True, blank=True, related_name='documento')
    
    produtor = models.ManyToManyField(Produtor, through='DocumentoProdutor')  
    assunto = models.ManyToManyField(Assunto, through='DocumentoAssunto')  
    pessoa = models.ManyToManyField(Pessoa, through='DocumentoPessoa')  
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Documento {self.titulo}"
    
    class Meta:
        db_table = "documento"
        verbose_name_plural = "Documentos"
        ordering = ['titulo']
        
        
class DocumentoProdutor(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE,)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE,)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Produtor: {self.produtor} Documento: {self.documento}'

    class Meta:
        unique_together = [['produtor', 'documento']]
        db_table = "documento_produtor"
        verbose_name_plural = "DocumentosProdutores"
        ordering = ['produtor']
        
        
class DocumentoAssunto(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE,)
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE,)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Assunto: {self.assunto} Documento: {self.documento}'

    class Meta:
        unique_together = [['assunto', 'documento']]
        db_table = "documento_assunto"
        verbose_name_plural = "DocumentosAssuntos"
        ordering = ['assunto']
        
        
class DocumentoPessoa(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE,)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pessoa: {self.pessoa} Documento: {self.documento}'

    class Meta:
        unique_together = [['pessoa', 'documento']]
        db_table = "documento_pessoa"
        verbose_name_plural = "DocumentosPessoas"
        ordering = ['pessoa']
        