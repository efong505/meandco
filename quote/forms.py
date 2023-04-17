from django import forms
from django.contrib.auth.models import User
from  .models import Quote

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']              


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']     

    def clean_email(self):
        data = self.cleaned_data['email']     
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already in use.")
        return data


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [ 'name', 'position', 'company', 'address', 
                  'phone', 'email', 'web_address', 'description', 
                  'priority', 'jobfile']

        
class QuoteEditForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [ 'name', 'position', 'company', 'address', 
                  'phone', 'email', 'web_address', 'description', 
                  'priority', 'jobfile', 'quoted_price', 'stat']
        
    
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    # to = forms.EmailField()
    subject = forms.CharField(max_length=25)
    message = forms.CharField(required=False,
                              widget=forms.Textarea)
    
