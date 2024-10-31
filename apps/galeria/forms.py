from apps.galeria.models import *
from django import forms
from datetime import date

class photo_form(forms.ModelForm):
    class Meta:
        model = photo
        exclude = ['published','user']
        labels = {
            'name':'Nome',
            'subtitle':'Legenda',
            'description':'Descrição',
            'image':'Image',
            'tag':'Categoria',
            'publish_date':'Data de publicação',
            'user':'Usuário'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'tag':forms.Select(attrs={'class':'form-control'}),
            'publish_date':forms.DateInput(

                format='%d/%m/%y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'user':forms.TextInput(attrs={'class':'form-control', 'disabled':True})
        }