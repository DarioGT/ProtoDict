from models import *

import globale.admin          
 
class ConceptInline(globale.admin.TabularInline):
    model = Concept 
    fk_name = 'model'
    extra = 1
    fields = ('code', 'description', 'conceptType', 'superConcept')


class Model_Admin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'code', 'description', 'modelType', 'superModel', 'domain' )
    fieldsets = (
        (None, {
            'fields': [('code', 'description')]
        }),
        ('Specifiques', {
            'fields': [('modelType', 'superModel', 'domain'),],
            'classes': ['collapse']
        }),
    )
    inlines = [
        ConceptInline,
        ]
    