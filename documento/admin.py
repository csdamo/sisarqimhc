from django.contrib import admin
from documento.models import Documento, DocumentoAssunto, DocumentoPessoa, DocumentoProdutor


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'titulo', 'data_inicial', 'data_final', 'ativo', 'genero_documental', 'nivel_permissao')
    list_display_links = ('id', 'codigo', 'titulo', 'data_inicial', 'data_final', 'ativo', 'genero_documental', 'nivel_permissao')
    list_filter = ('acervo', 'estrutura', 'nivel_permissao', 'genero_documental')
    search_fields = ('titulo',)

admin.site.register(Documento, DocumentoAdmin)


class DocumentoProdutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'produtor', 'documento')
    list_display_links = ('id', 'produtor', 'documento')

admin.site.register(DocumentoProdutor, DocumentoProdutorAdmin)


class DocumentoAssuntoAdmin(admin.ModelAdmin):
    list_display = ('id', 'assunto', 'documento')
    list_display_links = ('id', 'assunto', 'documento')

admin.site.register(DocumentoAssunto, DocumentoAssuntoAdmin)


class DocumentoPessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'documento')
    list_display_links = ('id', 'pessoa', 'documento')

admin.site.register(DocumentoPessoa, DocumentoPessoaAdmin)
