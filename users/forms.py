from django import forms

class login_form(forms.Form):
    login_name = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'João Silva'}
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class':'form-control',
                   'placeholder':'***********'}
        )
    )

class singup_form(forms.Form):
    singup_name = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'João Silva'}
        )
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={'class':'form-control',
                   'placeholder':'joaoisilva@example.com'}
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class':'form-control',
                   'placeholder':'***********'}
        )
    )
    password_conf = forms.CharField(
        label='Confirme sua Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'class':'form-control',
                   'placeholder':'Confirme sua senha'}
        )
    )