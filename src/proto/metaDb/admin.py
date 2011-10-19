# This is an auto-generated model module by CeRTAE OMS PlugIn
# for project : "Modelibra.py" >

from globale import admin
from models import *  
import globale.admin
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
#DGT: Invocacion de llave a 2 niveles  
#    list_filter y search_fields permiten  __lookup syntax, 
#    list_display obliga la definicion ya sea en el modelo o como funcion    

class PropertyAdmin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'model_concept', 'concept', 'code',  'description',  'baseType','superProperty', 'alias', 'physicalName')
    list_filter = ( 'concept__model', )
    search_fields = ( 'code', 'superProperty', 'alias', 'physicalName')


admin.site.register(Property, PropertyAdmin)

#---------------  

class RelationshipAdmin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'concept', 'baseConcept', 'code',  'description', 'alias')
    list_filter = ( 'concept', )
    search_fields = ( 'baseConcept', 'code',  'description', 'alias')


admin.site.register(Relationship, RelationshipAdmin)



class UdpAdmin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'metaObj', 'code', 'value')
#   list_filter = ( 'metaObj', )
    search_fields = ( 'code', 'value')


admin.site.register(Udp, UdpAdmin)


class MetaLinkAdmin(globale.admin.ModelAdmin):
    app_name = 'Proto'
    list_display =( 'metaLinkModel' , 'code', 'alias', 'destinationText', 'sourceCol', 'destinationCol')
    list_filter = ( 'metaLinkModel' , )
    search_fields = ( 'code', 'alias', 'destinationText', 'sourceCol', 'destinationCol')


admin.site.register(MetaLink, MetaLinkAdmin)

#admin.site.register(PropertyChoice)
#admin.site.register(NavigationLink)
#admin.site.register(EntryPoints)
#admin.site.register(Menu)
#admin.site.register(ModelGraphic)
#admin.site.register(Traduction)


class MetaObjAdmin(admin.ModelAdmin):
    list_display =( 'code', 'objType', 'description', 'category'  )
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

