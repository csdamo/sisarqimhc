from django.db import models

class Assunto(models.Model):

    titulo = models.CharField(max_length=255, unique=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Assunto {self.titulo}"

    class Meta:
        db_table = "assunto"
        verbose_name_plural = "Assuntos"
        ordering = ['titulo']
        

