from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=200)
    check = forms.BooleanField(required=False)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Imię i nazwisko')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Wiadomość')

class PasswordChange(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), label="Stare hasło")
    new_password = forms.CharField(widget=forms.PasswordInput(), label="Nowe hasło")
    new_password_again = forms.CharField(widget=forms.PasswordInput(), label="Powtórz hasło")

class ChangeEmailForm(forms.Form):
    email = forms.EmailField(label='Nowy email')