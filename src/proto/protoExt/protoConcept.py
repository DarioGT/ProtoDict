# -*- coding: utf-8 -*-

import sys

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import  Context
from django.template import  RequestContext
from django.template.loader import get_template 
from django.utils.translation import gettext as __
from protoExtJs import protoGrid, utils 
from protoExtJs.forms import ExtJsForm, getExtJsModelForm



from django.core import serializers
import django.utils.simplejson as json

def getDjangoModel(  modelName ):

#   llama directamente  
#    model = models.get_model( appCode, modelName )
    
    # Encuentra el modelo ( sin la app ) 
    for m in models.get_models():
        if m._meta.object_name.lower() == modelName.lower():
            model = m
            break

    return model 


# Create your views here.
def protoGetPCI(request):
    # used like this in the main urls.py :
    #(r'^apps/(?P<app>[^/]+)/(?P<view>[^/]+)$', 'core.appdispatcher.dispatch' ), --> apps/app/views.py/view
    #(r'^apps/(?P<app>[^/]+)/?$', 'core.appdispatcher.dispatch' ),               --> apps/app/views.py/default
    

    # if you have an EditableModelGrid then you can use POST data to update your instances.
    if request.method == 'GET':

#       protoApp  = request.POST.get('protoApp', '')
        protoConcept = request.GET.get('protoConcept', '')
        
        model = getDjangoModel(protoConcept)
        grid = protoGrid.ProtoGridFactory( model  )        

        pRows = model.objects.filter(pk = 0)
        pRowsCount = 0
        
        json = grid.to_grid(
                pRows, 
                totalcount = pRowsCount, 
                )
    
        resp = utils.JsonResponse(json)
        return resp
        
#        return HttpResponse(json.dumps(context), mimetype="application/json")


def protoGetList(request):
#   Vista simple para cargar la informacion, 
#   Buscar el modelo dinamicamente y cargar la info correspondiente    
    
    page = int(request.GET.get('page', 0))
    start = int(request.GET.get('start', 0))
    limit = int(request.GET.get('limit', 0))

#    total_contacts = Contact.objects.all().count()
    total_contacts = 0
#    contacts = Contact.objects.all()[start:limit*page]
    list = []
#    for contact in contacts:
#        list.append(model_to_dict(contact, fields=[field.name for field in contact._meta.fields]))
    context = {
        'total': total_contacts,
        'data': list,
        'success': True
    }
    return HttpResponse(json.dumps(context), mimetype="application/json")


