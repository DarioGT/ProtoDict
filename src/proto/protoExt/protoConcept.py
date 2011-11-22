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
    
    if request.method == 'GET':

#       protoApp  = request.POST.get('protoApp', '')
        protoConcept = request.GET.get('protoConcept', '')
        protoFilter = request.GET.get('protoFilter', '')
        protoFilterBase = request.GET.get('protoFilterBase', '')
        
#       page = int(request.GET.get('page', 0))
        start = int(request.GET.get('start', 0))
        limit = int(request.GET.get('limit', 100))

        sort = request.GET.get('sort', 'id')
        sort_dir = request.GET.get('dir', 'ASC')

    else:

#       protoApp  = request.POST.get('protoApp', '')
        protoConcept = request.POST.get('protoConcept', '')
        protoFilter = request.POST.get('protoFilter', '')
        protoFilterBase = request.POST.get('protoFilterBase', '')
        
#       page = int(request.GET.get('page', 0))
        start = int(request.POST.get('start', 0))
        limit = int(request.POST.get('limit', 100))

        sort = request.POST.get('sort', 'id')
        sort_dir = request.POST.get('dir', 'ASC')

        
        
#   Carga la info
    model = getDjangoModel(protoConcept)
    
#   Convierte el filtro en un diccionario 
    if (len (protoFilter) > 0 ):
        try: protoStmt = eval( protoFilter )
        except: protoStmt = {'pk':0}
    else: 
        protoStmt = {}

#   El filtro base viene en la configuracion MD 
    if (len (protoFilterBase) > 0 ):
        try: protoStmtBase = eval( protoFilterBase )
        except: protoStmtBase = {'pk':0}
    else: 
        protoStmtBase = {}

#   Obtiene las filas del modelo 
    pRows = model.objects.filter(**protoStmt ).filter(**protoStmtBase ).order_by('id')[start: limit]
    pRowsCount = pRows.count()


    pList = []
    for reg in pRows:
        pList.append(model_to_dict(reg, fields=[field.name for field in reg._meta.fields]))

#    pList = [{'id':1,'first':"Fred",'last':"Flintstone",'email':"fred@flintstone.com"},{'id':2,'first':"Wilma",'last':"Flintstone",'email':"wilma@flintstone.com"},{'id':3,'first':"Pebbles",'last':"Flintstone",'email':"pebbles@flintstone.com"},{'id':4,'first':"Barney",'last':"Rubble",'email':"barney@rubble.com"},{'id':5,'first':"Betty",'last':"Rubble",'email':"betty@rubble.com"},{'id':6,'first':"BamBam",'last':"Rubble",'email':"bambam@rubble.com"}]
    
    context = json.dumps({
            "success": True,
            'totalCount': pRowsCount,
            'rows': pList,
            })
    
    return HttpResponse(context, mimetype="application/json")

