from models import *

import globale.admin          
 
class ConceptInline(globale.admin.TabularInline):
    model = Concept 
    fk_name = 'model'
    extra = 1
    fields = ('code', 'description', 'category', 'superConcept')


fdsModel= ( 'code', 'category', 'description',  'modelPrefix', 'superModel', 'alias', 'physicalName' )
intModel= ( 'idModel', 'idRef' )

class Model_Admin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'code', 'description', 'alias', 'superModel', 'domain' )
    list_filter =(  'domain', 'superModel', )
    search_fields =('code', 'description', 'alias', 'superModel' )
    
    fieldsets = (
        (None, {
            'fields': [('code', 'description')]
        }),
        ('Specifiques', {
            'fields': [('category', 'superModel', 'domain'),],
            'classes': ['collapse']
        }),
    )
    inlines = [
        ConceptInline,
        ]
    