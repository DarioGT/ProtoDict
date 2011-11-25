# -*- coding: utf-8 -*-

#import sys

# Importa el sitio con las collecciones admin ya definidas 
from globale.admin.sites import  site

from django.conf import settings

from django.http import HttpResponse
import django.utils.simplejson as json


def getProtoExt( objBase   ):
    try: 
        protoExt = objBase.protoExt 
    except: 
        protoExt = {} 
    return protoExt 


def protoGetMenuData(request):
    """
    Displays the main admin index page, which lists all of the installed
    apps that have been registered in this site.
    """
    
    app_dict = {}
    ixApp = 1 
    ixMod = 1
     
#   user = request.user
    for model, model_admin in site._registry.items():

        protoAdmin = getProtoExt ( model_admin )
        protoModel = getProtoExt ( model )

        app_label = model._meta.app_label
        app_label = protoAdmin.get('app_name', app_label )

        menuApp = settings.MENU_APP.get( app_label, {} ) 

        if menuApp.get('hidden', False ): 
            continue 

        ixModAux = protoModel.get('menuIndex', protoAdmin.get( 'menuIndex', ixMod) )

        model_dict = {
            'id': model._meta.object_name,
            'text': model._meta.verbose_name.title() ,
            'index': ixModAux ,
            'leaf': True,
        }
        if app_label in app_dict:
            app_dict[app_label]['children'].append(model_dict)

        else:
            app_dict[app_label] = {
                'text': menuApp.get('title', app_label )  ,
                'expanded': menuApp.get('expanded', True) ,
                'index': menuApp.get('menuIndex', ixApp ),
                'children': [model_dict],
            }

            ixApp += 1
             
        ixMod += 1 

    # Sort the apps alphabetically.
    app_list = app_dict.values()
    app_list.sort(key=lambda x: x['index'])

    # Sort the models alphabetically within each app.
    for app in app_list:
        app['children'].sort(key=lambda x: x['index'])

    context = json.dumps( app_list ) 

    return HttpResponse( context, mimetype="application/json")
