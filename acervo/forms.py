from django import forms
from django.core.exceptions import ValidationError
from .models import Acervo

class AcervoForm(forms.ModelForm):

    class Meta:
        model = Acervo
        fields = [
            'codigo',
            'titulo',
            'sigla',
            'descricao',
            'info_adicionais',  
            'ordem_exibicao',
        ] 
		
        labels = {
            'codigo':'Código',
            'titulo':'Título',
            'sigla': 'Sigla',
            'descricao': 'Descrição',  
            'info_adicionais':'Informações Adicionais',
            'ordem_exibicao': 'Ordem de Exibição',
        }
        
           
    def clean_ordem_exibicao(self):
        ordem = self.cleaned_data.get("ordem_exibicao")
        
        if ordem <= 0:
            raise ValidationError('Ordem deve ser maior que zero.')
        else:
            existe_ordem = Acervo.objects.filter(ordem_exibicao=ordem).count()
            insert = self.instance.pk == None

            if insert:
                if existe_ordem != 0:
                    raise ValidationError('Ordem deve ser única.')
            else:
                if ordem != self.instance.ordem_exibicao:
                    if existe_ordem != 0:
                        raise ValidationError('Ordem deve ser única.')

        return ordem
    