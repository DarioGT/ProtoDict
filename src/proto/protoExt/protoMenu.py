# -*- coding: utf-8 -*-

#import sys

# Importa el sitio con las collecciones admin ya definidas 
from globale.admin.sites import  site

from django.conf import settings
from django.utils.text import capfirst

from django.http import HttpResponse
import django.utils.simplejson as json


def getMenuApp( name   ):
    try: 
        menuApp = settings.MENU_APP[ name ]
    except: 
        menuApp = {} 
    return menuApp 

def protoGetMenuData(request):
    """
    Displays the main admin index page, which lists all of the installed
    apps that have been registered in this site.
    """
    
    app_dict = {}
    ixApp = 0 
    ixMod = 0
     
#   user = request.user
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label

        menuApp = getMenuApp( app_label)
        if menuApp.get('hidden', False ): 
            continue 

        model_dict = {
            'id': model._meta.object_name,
            'text': model._meta.verbose_name.title() ,
            'index': ixMod,
            'leaf': True,
        }
        if app_label in app_dict:
            app_dict[app_label]['children'].append(model_dict)

        else:
            app_dict[app_label] = {
                'text': menuApp.get('title', app_label.title())  ,
                'expanded': menuApp.get('expanded', True) ,
                'index': menuApp.get('index', ixApp ),
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

    context = app_list 
#    {
#        'app_list': app_list,
#    }

    
#    context = [{
#                    'text':'Dictionaire de donnes',
#                    'expanded':True,
#                    'children':[
#                        { 'id': 'Concept' , 'text':'Elements des donnes', 'leaf':True },
#                        { 'id': 'Property' , 'text':'Proprietes',  'leaf':True },
#                    ]
#                }]

    return HttpResponse(json.dumps(context), mimetype="application/json")

