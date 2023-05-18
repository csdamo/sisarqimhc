from django import forms
from django.core.exceptions import ValidationError
from .models import Estrutura

class EstruturaForm(forms.ModelForm):

    class Meta:
        model = Estrutura
        fields = [
            'codigo',
            'titulo',
            'sigla',
            'descricao',
            'info_adicionais',  
            'acervo',
            'estrutura_nivel_superior'
        ] 
		
        labels = {
            'codigo':'Código',
            'titulo':'Título',
            'sigla': 'Sigla',
            'descricao': 'Descrição',  
            'info_adicionais':'Informações Adicionais',
            'acervo': 'Acervo',
            'estrutura_nivel_superior': 'Nível Superior'
        }
        
                   
    def clean_acervo(self):
        estrutura_nivel_superior = self.cleaned_data.get("estrutura_nivel_superior")
        acervo = self.cleaned_data.get("acervo")
        if estrutura_nivel_superior:
            acervo_nivel_superior = estrutura_nivel_superior.acervo
        else:
            acervo_nivel_superior = None
            
        if acervo != acervo_nivel_superior:
            raise ValidationError('O Acervo deve ser o mesmo do nível superior')
        
        return acervo
    
                       
    def clean_estrutura_nivel_superior(self):
        estrutura_nivel_superior = self.cleaned_data.get("estrutura_nivel_superior")
        insert = self.instance.pk == None
        
        if insert:
            if estrutura_nivel_superior == self.instance.estrutura_nivel_superior:
                raise ValidationError('Essa associação não é possível')
           

        return estrutura_nivel_superior
    