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
    app_name = 'Dictionnaire de donnees'
    list_display =( 'model', 'code',  'description',  'superConcept', )
    list_filter = ( 'model', 'superConcept', )
    search_fields = ( 'code', 'description',  'superConcept')

    fieldsets = (
        (None, {
            'fields': [('code', 'description', 'superConcept', 'model')]
        }),
    )
    inlines = [
        UpdInline,
        PropertyInline,
        RelationshipInline,
        ]

    