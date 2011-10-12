# This is an auto-generated model module by CeRTAE OMS PlugIn
# for project : "Modelibra" >
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order

from django.db import models
from django.utils.encoding import force_unicode

#datamodel name="Relational Data Model" idmodel="1" idref="0">


def strNotNull(  sValue ):
    if (sValue is None): 
        return "_"
    else: return sValue 

class MetaObj(models.Model):
    #OBJTYPE  = (('Domain', 'Domain'),('Model', 'Model'),('Concept', 'Concept'),('Property', 'Porperty'),('?', 'Unknown'),)
    code = models.CharField(verbose_name=u'code', blank = True, null = True, max_length=50 )
    objType = models.CharField(verbose_name=u'objType',  max_length=50)
    description = models.CharField(verbose_name=u'description', blank = True, null = True, max_length=50)

    def __unicode__(self):
        return self.code 

   
class Domain(MetaObj):
    #DOMAINTYPE=(('Analyses',(('MCD','Modeleconceptualdedonnes'),('MLD','Modellogique'),('MPD','Modelphisique'),)),('Interface',(('MSI','Modeledespecificaciond''interface'),('MSR','Modeledespecificacionderapports'),)),('unknown','Unknown'),)
    domainType = models.CharField(verbose_name=u'domainType', max_length=50)
    origin = models.CharField(verbose_name=u'origin', blank = True, null = True, max_length=50)
    superDomain = models.ForeignKey('Domain', blank = True, null = True)

    def save(self, *args, **kwargs ):
        self.objType = "Domain"
        super(Domain, self).save(*args, **kwargs) # Call the "real" save() method.
    
    def __unicode__(self):
        return self.code 


#DGT: Como manejar la seleccion de opciones dependiendo del padre, implementar el manejo de discretas 
class Model(MetaObj):
    #MODELTYPE=(('Analyses',(('MCD','Modeleconceptualdedonnes'),('MLD','Modellogique'),('MPD','Modelphisique'),)),('Interface',(('MSI','Modeledespecificaciond''interface'),('MSR','Modeledespecificacionderapports'),)),('unknown','Unknown'),)
    modelType = models.CharField(verbose_name=u'modelType', max_length=50)
    modelPrefix = models.CharField(verbose_name=u'modelPrefix', blank = True, null = True, max_length=50)
    modelIx = models.CharField(verbose_name=u'Ix', blank = True, null = True, max_length=50)
    modelRef = models.CharField(verbose_name=u'IxRef', blank = True, null = True, max_length=50)
    domain = models.ForeignKey('Domain')
    superModel = models.ForeignKey('Model', blank = True, null = True)

    def save(self, *args, **kwargs ):
        self.objType = "Model"
        super(Model, self).save(*args, **kwargs) # Call the "real" save() method.
    
    def __unicode__(self):
        return self.code 

class Concept(MetaObj):
    conceptType = models.CharField(verbose_name=u'conceptType', blank = True, null = True, max_length=50)
    model = models.ForeignKey('Model')
    superConcept = models.ForeignKey('Concept', blank = True, null = True)
    def __unicode__(self):
        return self.code 

    def save(self, *args, **kwargs ):
        self.objType = "Concept"
        super(Concept, self).save(*args, **kwargs) # Call the "real" save() method.


class Property(MetaObj):
    propertyType = models.CharField(verbose_name=u'propertyType', blank = True, null = True, max_length=50)
    classType = models.CharField(verbose_name=u'classType', blank = True, null = True, max_length=50)
    length = models.CharField(verbose_name=u'length', blank = True, null = True, max_length=50)
    decLength = models.CharField(verbose_name=u'decLength', blank = True, null = True, max_length=50)
    nullable = models.CharField(verbose_name=u'nullable', blank = True, null = True, max_length=50)
    required = models.CharField(verbose_name=u'required', blank = True, null = True, max_length=50)
    defaultValue = models.CharField(verbose_name=u'defaultValue', blank = True, null = True, max_length=50)
    sensitive = models.CharField(verbose_name=u'sensitive', blank = True, null = True, max_length=50)
    essential = models.CharField(verbose_name=u'essential', blank = True, null = True, max_length=50)
    unique = models.CharField(verbose_name=u'unique', blank = True, null = True, max_length=50)
    propertyIndex = models.CharField(verbose_name=u'propertyIndex', blank = True, null = True, max_length=50)

    #DGT: La derivacion deberia ser una referencia pero en la carga no es posible hacer la referencia se requiere un campo texto 
    # pero el mantenimiento deberia ser con la referencia, podria guardarse en discretas y un procedimiento posterior 
    # agregaria las referencias reales 
    derivationType = models.CharField(verbose_name=u'derivationType', blank = True, null = True, max_length=50)
    derivationRule = models.CharField(verbose_name=u'derivationRule', blank = True, null = True, max_length=50)
    derivationConcept = models.CharField(max_length=50,verbose_name=u'derivationConcept',  blank = True, null = True)
    derivationProperty = models.CharField(max_length=50,verbose_name=u'derivationProperty',  blank = True, null = True)

    concept = models.ForeignKey('Concept')
    superProperty = models.ForeignKey('Property', blank = True, null = True)

    def save(self, *args, **kwargs ):
        if self.objType <> "Relationship":
            self.objType = "Property"
        super(Property, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        sConcept = strNotNull(self.concept.code)
        sProperty = strNotNull(self.code)
        return sConcept + '.' + sProperty    


class Relationship(Property):
    relationType = models.CharField(verbose_name=u'relationType', blank = True, null = True, max_length=50)
    baseMin = models.CharField(verbose_name=u'baseMin', blank = True, null = True, max_length=50)
    baseMax = models.CharField(verbose_name=u'baseMax', blank = True, null = True, max_length=50)
    refMin = models.CharField(verbose_name=u'refMin', blank = True, null = True, max_length=50)
    refMax = models.CharField(verbose_name=u'refMax', blank = True, null = True, max_length=50)
    
    #DGT: Igual caso q las derivaciones de conceptos
    conceptRef = models.CharField(max_length=50, blank = True, null = True,)

    def save(self, *args, **kwargs ):
        self.objType = "Relationship"
        super(Relationship, self).save(*args, **kwargs) # Call the "real" save() method.

    def __unicode__(self):
        return (strNotNull(self.concept.code) + '.' + strNotNull(self.conceptRef))

class UserDefinedProperty(models.Model):
    udpCode = models.CharField(verbose_name=u'udpCode', blank = True, null = True, max_length=50)
    udpTarget = models.CharField(verbose_name=u'udpTarget', blank = True, null = True, max_length=50)
    udpType = models.CharField(verbose_name=u'udpType', blank = True, null = True, max_length=50)
    udpValue = models.CharField(verbose_name=u'udpValue', blank = True, null = True, max_length=50)
    udpRule = models.CharField(verbose_name=u'udpRule', blank = True, null = True, max_length=50)
    metaObj = models.ForeignKey('MetaObj')
    def __unicode__(self):
        return self.udpCode 

class MetaLink(models.Model):
    metaLinkType = models.CharField(verbose_name=u'synonymType', blank = True, null = True, max_length=50)
    metaLinkDescription = models.CharField(verbose_name=u'synonymDescription', blank = True, null = True, max_length=50)
    metaObjBase = models.ForeignKey('MetaObj', related_name='metaObjBase')
    metaObjRef = models.ForeignKey('MetaObj', related_name='metaObjRef')

    def __unicode__(self):
        return self.metaLinkDescription 

class NavigationLink(models.Model):
    navigationType = models.CharField(verbose_name=u'navigationType', blank = True, null = True, max_length=50)
    navigationRule = models.CharField(verbose_name=u'navigationRule', blank = True, null = True, max_length=50)
    caption = models.CharField(verbose_name=u'caption', blank = True, null = True, max_length=50)
    toolTip = models.CharField(verbose_name=u'toolTip', blank = True, null = True, max_length=50)
    tag = models.CharField(verbose_name=u'tag', blank = True, null = True, max_length=50)
    conceptBase = models.ForeignKey('Concept')
    conceptRef = models.ForeignKey('Concept', related_name='+')
    def __unicode__(self):
        return self.caption 

class EntryPoints(models.Model):
    caption = models.CharField(verbose_name=u'caption', blank = True, null = True, max_length=50)
    titre = models.CharField(verbose_name=u'titre', blank = True, null = True, max_length=50)
    typeEntryPoint = models.CharField(verbose_name=u'typeEntryPoint', blank = True, null = True, max_length=50)
    rule = models.CharField(verbose_name=u'rule', blank = True, null = True, max_length=50)
    concept = models.ForeignKey('Concept', blank=True, null=True)
    domain = models.ForeignKey('Domain')
    def __unicode__(self):
        return self.caption

class Menu(models.Model):
    menuCode = models.CharField(verbose_name=u'menuCode', blank = True, null = True, max_length=50)
    menuBase = models.CharField(verbose_name=u'menuBase', blank = True, null = True, max_length=50)
    menuIndex = models.CharField(verbose_name=u'menuIndex', blank = True, null = True, max_length=50)
    entryPoints = models.ForeignKey('EntryPoints')
    def __unicode__(self):
        return self.menuCode

class ModelGraphic(models.Model):
    modelName = models.CharField(verbose_name=u'modelName', blank = True, null = True, max_length=50)
    model = models.ForeignKey('Model')
    def __unicode__(self):
        return self.modelName

class Traduction(models.Model):
    languageCode = models.CharField(verbose_name=u'languageCode', blank = True, null = True, max_length=50)
    caption = models.CharField(verbose_name=u'caption', blank = True, null = True, max_length=50)
    description = models.CharField(verbose_name=u'description', blank = True, null = True, max_length=50)
    MetaObj = models.ForeignKey('MetaObj')
    def __unicode__(self):
        return self.languageCode

class PropertyChoice(models.Model):
    code = models.CharField(verbose_name=u'code', max_length=50 )
    value = models.CharField(verbose_name=u'value', blank = True, null = True, max_length=50)
    filtre = models.CharField(verbose_name=u'filtre', blank = True, null = True, max_length=50)
    tag = models.CharField(verbose_name=u'tag', blank = True, null = True, max_length=50)
    propertyField = models.ForeignKey('Property')
    def __unicode__(self):
        return (self.propertyField.code + '.' + self.code )  
