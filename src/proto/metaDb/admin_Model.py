from models import *

import globale.admin          
 
class ConceptInline(globale.admin.TabularInline):
    model = Concept 
    fk_name = 'model'
    extra = 1
    fields = ('code', 'description',  'superConcept')


fdsModel= ( 'code', 'category', 'description',  'modelPrefix', 'superModel', 'alias', 'physicalName' )
intModel= ( 'idModel', 'idRef' )

class Model_Admin(globale.admin.ModelAdmin):
    app_name = 'Dictionnaire de donnees'
    verbose_name_plural = 'Modeles' 
    list_display =(  'code', 'description','superModel', 'domain', 'physicalName')
    list_filter =(  'domain', 'superModel', )
    search_fields =('code', 'description', 'superModel', 'physicalName' )
    
    fieldsets = (
        (None, {
            'fields': [('code', 'description', 'domain')]
        }),
    )
    inlines = [
        ConceptInline,
        ]
    
    protoExt = {}
    protoExt[ 'protoDetails' ] = [
        {'menuText': 'Entite', 'conceptDetail': 'metaDb.Concept', 'detailField': 'model__pk', 'masterField': 'pk'},
        {'menuText': 'Udp', 'conceptDetail': 'metaDb.Udp', 'detailField': 'metaObj__pk', 'masterField': 'pk'}, 
        ]

    
#    [{
#            "menuText": "Concept", 
#            "conceptDetail": "metaDb.Concept", 
#            "masterField": "id",
#            "detailField": "model__id"
#            },]
#    
    
    