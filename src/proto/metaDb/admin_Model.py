from models import *

import globale.admin          
 
class ConceptInline(globale.admin.TabularInline):
    model = Concept 
    fk_name = 'model'
    extra = 1
    fields = ('code', 'description', 'category', 'superConcept')


class Model_Admin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'code', 'description', 'category', 'superModel', 'domain' )
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
    