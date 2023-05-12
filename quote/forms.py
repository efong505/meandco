from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from  .models import Quote


"""
LOGIN FORM - Used for logging into their account 
"""
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


"""
REGISTRATION FORM - Form that allows the user to create an account with choosing
    a username, entering the first name and email address. 
    The class also checks to see if the passwords being entered match. If not
    it returns an error message saying that the passwords don't match. 
"""
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


"""
QUOTE FORM - Form that allows the user to create a quote request 
    submission that has the user provide a name, their position, 
    the company name, the address, the phone number, email addres,
    the current or intended website, a description textfield to 
    allow the user to state what they're looking for and also
    upload a file along with their submission. 
"""
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [ 'name', 'position', 'company', 'address', 
                  'phone', 'email', 'web_address', 'description', 
                  'priority', 'jobfile', 'stat']

        
"""
QUOTE EDIT FORM - This form allows the superadmin or any user placed in the "Testing"
    group to edit existing forms. 
"""
class QuoteEditForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [ 'name', 'position', 'company', 'address', 
                  'phone', 'email', 'web_address', 'description', 
                  'priority', 'jobfile', 'quoted_price', 'stat','quoted' , 'requester']
        

"""
EMAIL FORM - This form is on the contact page and it allows the user to enter their name, 
    email address, a subject and their message. 
"""   
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    # to = forms.EmailField()
    subject = forms.CharField(max_length=25)
    message = forms.CharField(required=False,
                              widget=forms.Textarea)
    captcha = CaptchaField()
