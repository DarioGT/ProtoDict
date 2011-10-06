from models import *

import globale.admin          
 
class ModelInline(globale.admin.TabularInline):
    model = Model
    fk_name = 'domain'
    extra = 1
    fields = ('code', 'description', 'modelType', 'superModel', 'domain')


class DomainAdmin(globale.admin.ModelAdmin):
    list_display =( 'code', 'description', 'domainType'  )
    fieldsets = (
        (None, {
            'fields': [('code', 'description')]
        }),
        ('Specifiques', {
            'fields': [('domainType', 'origin'), 
                       ('superDomain')]
        }),
    )
    inlines = [
        ModelInline,
        ]