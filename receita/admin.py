from django.contrib import admin
from django import forms

from .models import *

from redactor.widgets import RedactorEditor

admin.site.site_header = "Danúbio"
admin.site.site_title = "Danúbio"
admin.site.index_title = "Gerenciamento da Danúbio"
admin.site.register(Unidade)

class ReceitaAdminForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'
        widgets = {
            'descricao' : RedactorEditor(),
        }

class IngredientesInline(admin.TabularInline):
    model = IngredienteReceita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    inlines = (IngredientesInline, )
    search_fields = ('produto__nome',)
    form = ReceitaAdminForm
    list_display = (
        'produto',
        'rendimento',
        'ingredientes_count',
        'custo',
        'preco_sugerido',
        'custo_por_rendimento',
        'preco_sugerido_por_rendimento',
    )

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade', 'preco')
    list_filter = ('unidade__nome',)
