from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'maxlength': '30'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'maxlength': '254'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'maxlength': '150'}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'minlength': '8'}))
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'minlength': '8'}), label="Confirmar Senha")
    
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
