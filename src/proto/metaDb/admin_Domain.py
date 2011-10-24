from models import *

import globale.admin          


 
class ModelInline(globale.admin.TabularInline):
    model = Model
    fk_name = 'domain'
    extra = 1
    fields =  ('code', 'description', 'superModel', 'domain')


class DomainAdmin(globale.admin.ModelAdmin):
    app_name = 'Dictionnaire de donnees'
    list_display =( 'code', 'description', )
    fieldsets = (
        (None, {
            'fields': [('code', 'description','origin', 'superDomain',)]
        }),
    )
    inlines = [
        ModelInline,
        ]