# This is an auto-generated model module by CeRTAE OMS PlugIn
# for project : "Modelibra.py" >

import globale.admin
from models import *


class MetaObjAdmin(globale.admin.ModelAdmin):
    list_display =( 'code', 'objType', 'description'  )
    readonly_fields = ('objType', )

    #Add = False  
    def has_add_permission(self, request):
        return False

    #Delete = False 
    def has_delete_permission(self, request, obj=None):
        return False

    #Update = False 
    def has_change_permission(self, request, obj=None):
        return False
                
globale.admin.site.register(MetaObj, MetaObjAdmin)

from adminDomain import DomainAdmin 
globale.admin.site.register(Domain, DomainAdmin)


globale.admin.site.register(Model)
globale.admin.site.register(Concept)
#--------------------------------------------- admin.site.register(Relationship)
#------------------------------------------------- admin.site.register(Property)
#-------------------------------------- admin.site.register(UserDefinedProperty)
#------------------------------------------------- admin.site.register(MetaLink)
#------------------------------------------- admin.site.register(NavigationLink)
#---------------------------------------------- admin.site.register(EntryPoints)
#----------------------------------------------------- admin.site.register(Menu)
#--------------------------------------------- admin.site.register(ModelGraphic)
#----------------------------------------------- admin.site.register(Traduction)
