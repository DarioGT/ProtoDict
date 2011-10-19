from models import *

import globale.admin          
 
class PropertyInline(globale.admin.TabularInline):
    model = Property 
    fk_name = 'concept'
    extra = 1
    fields = ('code', 'description', 'baseType')

class RelationshipInline(globale.admin.TabularInline):
    model = Relationship 
    fk_name = 'concept'
    extra = 1
    fields = ('code', 'description',  'baseConcept')


class Concept_Admin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'model', 'code', 'category', 'description',  'superConcept', 'alias', 'physicalName', )
    list_filter = ( 'model', 'superConcept', )
    search_fields = ( 'code', 'category', 'description',  'superConcept', 'alias', 'physicalName')

    fieldsets = (
        (None, {
            'fields': [('code', 'description')]
        }),
        ('Specifiques', {
            'fields': [('category', 'superConcept', 'model'),]
        }),
    )
    inlines = [
        PropertyInline,
        RelationshipInline,
        ]

    