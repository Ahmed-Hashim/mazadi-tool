
from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=('fullname','bio','profile_pic','phone_number','gender','country','timezone','address','facebook_url','instagram_url','twitter_url','linkedin_url','skype_url')

        widgets={
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
            'timezone': forms.Select(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class':'form-control'}),
            'skype_url': forms.TextInput(attrs={'class':'form-control'}),


        }
class UserUpdateForm(forms.ModelForm):
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    #password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    
    class Meta:
        model = User
        fields = ['username', 'email',  'first_name', 'last_name']   

class ChangePassword(forms.ModelForm):
    

    password1=forms.CharField(label='Password',min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','name':'password1'}))
    password2=forms.CharField(label='Confirm Password',min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','name':'password2'}))
    password=forms.CharField(label='Old Password',min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','name':'password'}))
    
    
    
    
    class Meta:
        model = User
        fields = ['password1','password2','password']   