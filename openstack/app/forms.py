
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class multitierForm(forms.Form):
    authurl = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "authurl",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    webservers = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1,2..",                
                "class": "form-control"
            }
        ))
    appservers = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1,2..",                
                "class": "form-control"
            }
        ))
    database = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1,2..",                
                "class": "form-control"
            }
        ))

class twotierForm(forms.Form):
    authurl = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "authurl",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    webservers = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1,2..",                
                "class": "form-control"
            }
        ))
    database = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "1,2..",                
                "class": "form-control"
            }
        ))
class codeForm(forms.Form):
    code = forms.CharField(
        widget=forms.Textarea(attrs={"rows":6, "cols":18}))

class databaseForm(forms.Form):
    ipaddress = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "10.0.2.0",                
                "class": "form-control"
            }
        ))

    databasename = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "mysql",                
                "class": "form-control"
            }
        ))
class rulesForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "secgroupdata",                
                "class": "form-control"
            }
        ))

    protocole = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "tcp",                
                "class": "form-control"
            }
        ))
    port = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "22",                
                "class": "form-control"
            }
        ))
    