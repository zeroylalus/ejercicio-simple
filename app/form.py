from django import forms

class animales (forms.Form):

    nombre = forms.CharField(label='', max_length=200,widget=forms.TextInput(attrs = {
        'class':'form',
        'style':'width: 900px;',
        'placeholder': 'nombre del animal'
    } ))




class atributos (forms.Form):
    
    animal = forms.IntegerField(label='',widget=forms.TextInput(attrs = {
        'class':'form',
        'style':'width: 900px;',
        'placeholder': 'id del animal'
    } ))

    descripcion = forms.CharField(label='', max_length=200,widget=forms.TextInput(attrs = {
        'class':'form',
        'style':'width: 900px;',
        'placeholder': 'descripción del animal'
    } ))