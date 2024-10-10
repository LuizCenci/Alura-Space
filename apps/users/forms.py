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
    first_name = forms.CharField(
        label='Primeiro nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'João'}
        )
    )
    surname = forms.CharField(
        label='Sobrenome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'Silva'}
        )
    )
    register_name = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'joaosilva'}
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

    def clean_register_name(self):
        name = self.cleaned_data.get('register_name')
        if name:
            name = name.strip()
            if ' ' in name:
                raise forms.ValidationError('O username não deve conter espaços entre as letras!')
            else:
                return name

    def clean_password_conf(self):
         password_1 = self.cleaned_data.get('password')      
         password_2 = self.cleaned_data.get('password_conf')  
         if password_1 and password_2:
              if password_1 != password_2:
                   raise forms.ValidationError('As senhas devem ser iguais!')    
              return password_2