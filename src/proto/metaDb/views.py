# -*- encoding: UTF-8 -*-
#
import sys

from django.db import models

from django.contrib.auth.models import User
from django import forms
             

from django.http import HttpResponse, HttpResponseRedirect
from django.template import  Context
from django.template import  RequestContext
from django.template.loader import get_template 

from protoExtJs import protoGrid, utils 
from protoExtJs.forms import ExtJsForm, getExtJsModelForm

def getDjangoModel(  appCode, modelName ):

#   llama directamente  
    model = models.get_model( appCode, modelName )
    
    # Encuentra el modelo 
#    for m in models.get_models():
#        if m._meta.object_name.lower() == modelName.lower():
#            model = m
#            break

    return model 


# Create your views here.
def protoGridDefinition(request):
    # used like this in the main urls.py :
    #(r'^apps/(?P<app>[^/]+)/(?P<view>[^/]+)$', 'core.appdispatcher.dispatch' ), --> apps/app/views.py/view
    #(r'^apps/(?P<app>[^/]+)/?$', 'core.appdispatcher.dispatch' ),               --> apps/app/views.py/default
    

    # if you have an EditableModelGrid then you can use POST data to update your instances.
    if request.method == 'POST':

        protoFilter = request.POST.get('protoFilter', '')
        protoFilterBase = request.POST.get('protoFilterBase', '')
        protoApp  = request.POST.get('protoApp', '')
        protoConcept = request.POST.get('protoConcept', '')
        
#        TODO: Independizar el llamado de la meta y de los datos 
#        protoModelLoad = request.POST.get('protoConcept', '1')

        model = getDjangoModel(protoApp,  protoConcept)
        grid = protoGrid.ProtoGridFactory( model  )        

        # handle save of grid data !
        if request.POST.get('delete', '')!='':

            modelName = request.GET.items()[0]

            dels = request.POST['delete'].split(',')
            User.objects.filter(id__in = dels).delete()
            return utils.JsonSuccess()
            # delete selected rows
            
        if request.POST.get('update', '')!='':    
            # update rows data (update+inserts)
            if 1: #try:
                grid.update_instances_from_json(request.POST['update'])
                return utils.JsonSuccess()
            else: #except:
                #print "Unexpected error:", sys.exc_info()[0]
                msg = getattr(sys.exc_info()[1], 'message', sys.exc_info()[0])
                #.message
                return utils.JsonError(str(msg))


    
        # parametros de trabajo  ( vienen en baseparam ) 
        start = request.POST.get('start', 0)
        limit = request.POST.get('limit', 20)
        sort = request.POST.get('sort', 'id')
        sort_dir = request.POST.get('dir', 'ASC')
    
        # Convierte el filtro en un diccionario 
        if (len (protoFilter) > 0 ):
            try: protoStmt = eval( protoFilter )
            except: protoStmt = {'pk':0}
        else: 
            protoStmt = {}

        # El filtro base viene en la configuracion MD 
        if (len (protoFilterBase) > 0 ):
            try: protoStmtBase = eval( protoFilterBase )
            except: protoStmtBase = {'pk':0}
        else: 
            protoStmtBase = {}
    
        # Obtiene las filas del modelo 
#        pRowsCount = model.objects.filter(**protoStmt ).count()
#        pRows = model.objects.filter(**protoStmt ).order_by('id')[start: limit]

        pRows = model.objects.filter(**protoStmt ).filter(**protoStmtBase ).order_by('id')
        pRowsCount = pRows.count()
        
        json = grid.to_grid(
                                pRows, 
                                start = start, 
                                limit =  limit, 
                                totalcount = pRowsCount, 
                                sort_field = sort, 
                                sort_direction = sort_dir
                                )
    
        resp = utils.JsonResponse(json)
        return resp


