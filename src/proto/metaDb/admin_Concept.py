from models import *

import globale.admin          
 
class PropertyInline(globale.admin.TabularInline):
    model = Property 
    fk_name = 'concept'
    extra = 1
    fields = ('code', 'description', 'classType')

class RelationshipInline(globale.admin.TabularInline):
    model = Relationship 
    fk_name = 'conceptBase'
    extra = 1
    fields = ('code', 'description', 'classType', 'conceptRef')


class Concept_Admin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'code', 'description', 'conceptType', 'superConcept', 'model' )
    fieldsets = (
        (None, {
            'fields': [('code', 'description')]
        }),
        ('Specifiques', {
            'fields': [('conceptType', 'superConcept', 'model'),]
        }),
    )
    inlines = [
        PropertyInline,
        RelationshipInline,
        ]

    