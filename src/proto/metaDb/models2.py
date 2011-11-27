from django.db import models


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


class NavigationLink(models.Model):
    navigationType = models.CharField(verbose_name=u'navigationType', blank = True, null = True, max_length=50)
    navigationRule = models.CharField(verbose_name=u'navigationRule', blank = True, null = True, max_length=50)
    caption = models.CharField(verbose_name=u'caption', blank = True, null = True, max_length=50)
    toolTip = models.CharField(verbose_name=u'toolTip', blank = True, null = True, max_length=50)
    tag = models.CharField(verbose_name=u'tag', blank = True, null = True, max_length=50)
    concept= models.ForeignKey('Concept')
    refConcept = models.ForeignKey('Concept', related_name='+')
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




# Prueba para generar los MasterDetail 

class Tabla1(models.Model):
    code1 = models.CharField(blank = True, null = True, max_length=200 )

class Tabla11(models.Model):
    code1 = models.CharField(blank = True, null = True, max_length=200 )
    tabla1a = models.ForeignKey('Tabla1', related_name= 'prueba1a')
    tabla1b = models.ForeignKey('Tabla1', related_name= 'prueba1b')
    tabla1c = models.ForeignKey('Tabla1', related_name= '+')
    

class Tabla12(models.Model):
    code1 = models.CharField(blank = True, null = True, max_length=200 )
    tabla1a = models.ForeignKey('Tabla1')

