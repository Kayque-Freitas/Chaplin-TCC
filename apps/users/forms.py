from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'maxlength': '30'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'maxlength': '254'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'maxlength': '150'}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'minlength': '8'}))
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'minlength': '8'}), label="Confirmar Senha")
    
    role = forms.ChoiceField(choices=[('gestor', 'Gestor da Equipe'), ('admin', 'Admin do Prédio')], widget=forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg'}))
    cpf = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'placeholder': '000.000.000-00'}))
    cnpj = forms.CharField(max_length=18, required=False, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'placeholder': '00.000.000/0000-00'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "As senhas não coincidem.")
        
        return cleaned_data

class EmailVerificationForm(forms.Form):
    code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={
        'class': 'w-full text-center text-3xl tracking-[1em] px-4 py-3 border border-gray-300 rounded-lg font-mono focus:ring-2 focus:ring-orange-500 focus:border-transparent',
        'placeholder': '000000',
        'maxlength': '6'
    }))
