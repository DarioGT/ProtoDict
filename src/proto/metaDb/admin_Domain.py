from models import *

import globale.admin          
 
class ModelInline(globale.admin.TabularInline):
    model = Model
    fk_name = 'domain'
    extra = 1
    fields = ('code', 'description', 'category', 'superModel', 'domain')


class DomainAdmin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'code', 'description', 'category'  )
    fieldsets = (
        (None, {
            'fields': [('code', 'description')]
        }),
        ('Specifiques', {
            'fields': [('category', 'origin'), 
                       ('superDomain')],
            'classes': ['collapse']
        }),
    )
    inlines = [
        ModelInline,
        ]