# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import multitierForm
from .forms import twotierForm
from .forms import codeForm
from .forms import databaseForm
from .forms import rulesForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
import os
import socket
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def multitier_view(request):
    form = multitierForm(request.POST or None)
    form1 = codeForm(request.POST or None)
    err =""
    msg = "fill to create a topology"
    msg1 = "if you want to execute your own configuration just drag click on the right buttom"

    if request.method == "POST":
        if form.is_valid():
            authurl = form.cleaned_data.get("authurl")
            password = form.cleaned_data.get("password")
            websevers = form.cleaned_data.get("webservers")
            appservers = form.cleaned_data.get("appservers")
            database = form.cleaned_data.get("database")
            variables = '-var="auth_url=%s" -var="passwd=%s" -var="count_web=%s" -var="count_data=%s" -var="count_app=%s"'%(authurl,password,websevers,database,appservers)  
            run ='terraform -chdir=3tier init ; terraform -chdir=3tier plan  %s ;terraform -chdir=3tier apply -auto-approve %s ;terraform -chdir=3tier init ; terraform -chdir=3tier plan  %s ;terraform -chdir=3tier apply -auto-approve %s '%(variables,variables,variables,variables)
            os.system(run)
            msg="topology created "
        elif form1.is_valid():
                code = form1.cleaned_data.get("code")
                file1 = open("configuration.yaml", "w")
                file1.write('%s'%code)
                file1.close()
                msg1="you have executed your own configuration"
                err=os.system('ansible-playbook configuration.yaml')
        else:
            msg = 'Error validating the form'    

    return render(request, "3tier.html",  {"form": form,"form1": form1 , "msg" : msg,"msg1" : msg1,"err" : err})

def twotier_view(request):
    form = twotierForm(request.POST or None)
    form1 = codeForm(request.POST or None)
    err =""
    msg = "fill to create a topology"
    msg1 = "if you want to execute your own configuration just drag click on the right buttom"
    if request.method == "POST":
        if form.is_valid():
            if 'create' in request.POST:
                authurl = form.cleaned_data.get("authurl")
                password = form.cleaned_data.get("password")
                websevers = form.cleaned_data.get("webservers")
                database = form.cleaned_data.get("database")
                variables = '-var="auth_url=%s" -var="passwd=%s" -var="count_web=%s" -var="count_data=%s"'%(authurl,password,websevers,database)  
                run ='terraform -chdir=2tier init ; terraform -chdir=2tier plan -auto-approve %s ;terraform -chdir=2tier apply -auto-approve %s ; terraform -chdir=2tier plan -auto-approve %s ;terraform -chdir=2tier apply -auto-approve %s'%(variables,variables,variables,variables)
                os.system(run)
                msg="topology created "
        elif form1.is_valid():
                code = form1.cleaned_data.get("code")
                file1 = open("configuration.yaml", "w")
                file1.write('%s'%code)
                file1.close()
                msg1="you have executed your own configuration"
                err=os.system('ansible-playbook configuration.yaml')
        else:
            msg = 'Error validating the form'    

    return render(request, "2tier.html", {"form": form,"form1": form1 , "msg" : msg,"msg1" : msg1,"err" : err})

def database_view(request):
    form = databaseForm(request.POST or None)
    form1 = codeForm(request.POST or None)
    err =""
    msg = "   fill to configure your database "
    msg1 = "if you want to execute your own configuration just drag click on the right buttom"
    if request.method == "POST":
        if form.is_valid():
            if 'submit' in request.POST:
                ipaddress = form.cleaned_data.get("authurl")
                databasename = form.cleaned_data.get("databasename")
                msg = "%s installed"%(databasename)
        elif form1.is_valid():
                code = form1.cleaned_data.get("code")
                file1 = open("configuration.yaml", "w")
                file1.write('%s'%code)
                file1.close()
                msg1="you have executed your own configuration"
                err=os.system('ansible-playbook configuration.yaml')
        else:
            msg = 'Error validating the form'    

    return render(request, "compute.html", {"form": form,"form1": form1 , "msg" : msg,"msg1" : msg1,"err" : err})

def rules_view(request):
    form = rulesForm(request.POST or None)
    form1 = codeForm(request.POST or None)
    err =""
    msg = "   fill to add a rule"
    msg1 = "if you want to execute your own configuration just drag click on the right buttom"
    if request.method == "POST":
        if form.is_valid():
            if 'add' in request.POST:
                name = form.cleaned_data.get("name")
                protocole = form.cleaned_data.get("protocole")
                port = form.cleaned_data.get("port")
                msg = "rule added "
                variables="openstack security group rule create --protocol %s --dst-port %s %s"%(protocole,port,name)
                os.system(variables)
        elif form1.is_valid():
                code = form1.cleaned_data.get("code")
                file1 = open("configuration.yaml", "w")
                file1.write('%s'%code)
                file1.close()
                msg1="you have executed your own configuration"
                err=os.system('ansible-playbook configuration.yaml')
        else:
            msg = 'Error validating the form'    

    return render(request, "security.html", {"form": form,"form1": form1 , "msg" : msg,"msg1" : msg1,"err" : err})
def healthcheck_view(request):
    msg=''
    #msg=os.popen('openstack security group show secgroup_app --max-width 0 --fit-width | tr "/n" "<br>"').read()
    return render(request, "index.html", {"msg" : msg})
