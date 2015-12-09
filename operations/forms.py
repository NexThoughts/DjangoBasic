from django import forms

class loginform(forms.Form):
    username=forms.EmailField(max_length=70,required=True,widget=forms.EmailInput(attrs={'class':'form-control'}),error_messages={'required':'please input email'})
    password=forms.CharField(max_length=70,required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
