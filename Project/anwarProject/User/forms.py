from django import forms

class loginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email '}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class post_form(forms.Form):
    user_name =forms.CharField(required=False,widget=forms.DateInput(attrs={'Placeholder':'User Name'}))
    post_date=forms.DateField(widget=forms.DateInput(attrs={'Placeholder':'Post Date'}))
    Enter_Post =forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder': 'Enter Post'}))
    

