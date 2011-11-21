
# -*- coding: utf-8 -*-

#import sys


from django.http import HttpResponse
import django.utils.simplejson as json

def protoGetMenuData(request):
    context = [{
                    'text':'Dictionaire de donnes',
                    'expanded':True,
                    'children':[
                        { 'id': 'Concept' , 'text':'Elements des donnes', 'leaf':True },
                        { 'id': 'Property' , 'text':'Proprietes',  'leaf':True },
                    ]
                }]

    return HttpResponse(json.dumps(context), mimetype="application/json")

