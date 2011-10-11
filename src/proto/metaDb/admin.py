# This is an auto-generated model module by CeRTAE OMS PlugIn
# for project : "Modelibra.py" >

from globale import admin
from models import * 

#---------------

from admin_Domain import DomainAdmin 
admin.site.register(Domain, DomainAdmin)


#---------------

from admin_Model import Model_Admin 
admin.site.register(Model, Model_Admin)

#---------------

from admin_Concept import Concept_Admin 
admin.site.register(Concept, Concept_Admin)

#---------------

admin.site.register(Relationship)
admin.site.register(Property)
admin.site.register(PropertyChoice)
admin.site.register(UserDefinedProperty)
admin.site.register(MetaLink)
admin.site.register(NavigationLink)
admin.site.register(EntryPoints)
admin.site.register(Menu)
admin.site.register(ModelGraphic)
#admin.site.register(Traduction)


class MetaObjAdmin(admin.ModelAdmin):
    list_display =( 'code', 'objType', 'description'  )
    readonly_fields = ('objType', )
    app_name = 'Meta'

    #Add = False  
    def has_add_permission(self, request):
        return False

    #Delete = False 
    def has_delete_permission(self, request, obj=None):
        return False

    #Update = False 
    def has_change_permission(self, request, obj=None):
        return True
                
admin.site.register(MetaObj, MetaObjAdmin)

