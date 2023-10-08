from django import forms
from .models import BlogUser
from .models import tinksPost
from .models import TweetComment
from .models import ReportManagement
from .models import BanUser
from .models import RemoveBan

class RegisterForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}),max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),max_length=50)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}))

    class Meta:
        model = BlogUser
        fields = ['username', 'first_name','last_name','email','password' ]

        help_texts ={
            "username": None

        }


class UserUpdateProfileForm(forms.ModelForm):
    avatar = forms.FileField(widget=forms.FileInput(attrs={'text': ""}),max_length=100,required=False)
    username = forms.CharField(max_length=50,required=False)
    first_name = forms.CharField(max_length=50,required=False)
    last_name = forms.CharField(max_length=50,required=False)
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'belirtilmedi','type':'date'}),required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-class','type': 'password'}),required=False)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Belirtilmedi'}),max_length=50,required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Belirtilmedi'}),max_length=50,required=False)
    educational_process =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Belirtilmedi'}),max_length=255,required=False)
    aboutme =forms.Textarea()
    class Meta:
        model = BlogUser
        fields =['avatar','username', 'first_name', 'last_name','birthdate', 'email', 'country',
                 'city','educational_process','aboutme']
        exclude = ['password']

        
class UpdateTweetForm(forms.ModelForm):
    
    class Meta:
        model = tinksPost
        fields =['post']


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = TweetComment
        fields =['message']       

class UpdateCommentForm(forms.ModelForm):
    
    class Meta:
        model = TweetComment
        fields =['message']

class ReportUserForm(forms.ModelForm):
    class Meta:
        model = ReportManagement
        fields =['reportMessage']  

class BanUserForm(forms.ModelForm):
    class Meta:
        model = BanUser
        fields =['banReason']

class RemoveBanForm(forms.ModelForm):
    class Meta:
        model = RemoveBan
        fields = ['removebanReason']