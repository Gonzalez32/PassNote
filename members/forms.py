from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))
    first_name = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'input'}))
    last_name = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'