# This is an auto-generated model module by CeRTAE OMS PlugIn
# for project : "project" >
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order

from django.db import models
from django.utils.encoding import force_unicode


#datamodel name="Relational Data Model" idmodel="1" idref="0">
class DomainBase(models.Model):
    code = models.CharField(verbose_name=u'code',max_length=50)
    type = models.CharField(verbose_name=u'type',max_length=50, blank = True, null = True)
    packageCode = models.CharField(verbose_name=u'packageCode',max_length=50, blank = True, null = True)
    abtraction = models.CharField(verbose_name=u'abtraction',max_length=50, blank = True, null = True)
    defaultContrunct = models.CharField(verbose_name=u'defaultContrunct',max_length=50, blank = True, null = True)
    packagePrefix = models.CharField(verbose_name=u'packagePrefix',max_length=50, blank = True, null = True)
    referenceModel = models.CharField(verbose_name=u'referenceModel',max_length=50, blank = True, null = True)
    i18n = models.CharField(verbose_name=u'i18n',max_length=50, blank = True, null = True)
    signin = models.CharField(verbose_name=u'signin',max_length=50, blank = True, null = True)
    signinConcept = models.CharField(verbose_name=u'signinConcept',max_length=50, blank = True, null = True)
    shortTextDefaultLength = models.CharField(verbose_name=u'shortTextDefaultLength',max_length=50, blank = True, null = True)
    pageBlockDefaultSize = models.CharField(verbose_name=u'pageBlockDefaultSize',max_length=50, blank = True, null = True)
    validateForm = models.CharField(verbose_name=u'validateForm',max_length=50, blank = True, null = True)
    confirmRemove = models.CharField(verbose_name=u'confirmRemove',max_length=50, blank = True, null = True)
    def __unicode__(self):
        return self.code

class DomainModel(models.Model):
    code = models.CharField(verbose_name=u'code',max_length=50)
    abstraction = models.CharField(verbose_name=u'abstraction',max_length=50, blank = True, null = True)
    extension = models.CharField(verbose_name=u'extension',max_length=50, blank = True, null = True)
    ExtensionDomain = models.CharField(verbose_name=u' extensionDomain',max_length=50, blank = True, null = True)
    extensionDomainType = models.CharField(verbose_name=u'extensionDomainType',max_length=50, blank = True, null = True)
    extensionModel = models.CharField(verbose_name=u'extensionModel',max_length=50, blank = True, null = True)
    author = models.CharField(verbose_name=u'author',max_length=50, blank = True, null = True)
    packageCode = models.CharField(verbose_name=u'packageCode',max_length=50, blank = True, null = True)
    persistent = models.CharField(verbose_name=u'persistent',max_length=50, blank = True, null = True)
    presistenceType = models.CharField(verbose_name=u'presistenceType',max_length=50, blank = True, null = True)
    presistenceRelativePath = models.CharField(verbose_name=u'presistenceRelativePath',max_length=50, blank = True, null = True)
    persistenceConfig = models.CharField(verbose_name=u'persistenceConfig',max_length=50, blank = True, null = True)
    defaultLoadSave = models.CharField(verbose_name=u'defaultLoadSave',max_length=50, blank = True, null = True)
    datePattern = models.CharField(verbose_name=u'datePattern',max_length=50, blank = True, null = True)
    session = models.CharField(verbose_name=u'session',max_length=50, blank = True, null = True)
    DomainBase = models.ForeignKey('DomainBase')
    def __unicode__(self):
        return self.code

class Concept(models.Model):
    code = models.CharField(verbose_name=u'code',max_length=50)
    abstraction = models.CharField(verbose_name=u'abstraction',max_length=50, blank = True, null = True)
    extension = models.CharField(verbose_name=u'extension',max_length=50, blank = True, null = True)
    extensionDomain = models.CharField(verbose_name=u'extensionDomain',max_length=50, blank = True, null = True)
    extensionDomainType = models.CharField(verbose_name=u'extensionDomainType',max_length=50, blank = True, null = True)
    extensionModel = models.CharField(verbose_name=u'extensionModel',max_length=50, blank = True, null = True)
    extensionConcept = models.CharField(verbose_name=u'extensionConcept',max_length=50, blank = True, null = True)
    extensionWithNeighbors = models.CharField(verbose_name=u'extensionWithNeighbors',max_length=50, blank = True, null = True)
    entitiesCode = models.CharField(verbose_name=u'entitiesCode',max_length=50, blank = True, null = True)
    packageCode = models.CharField(verbose_name=u'packageCode',max_length=50, blank = True, null = True)
    min = models.CharField(verbose_name=u'min',max_length=50, blank = True, null = True)
    max = models.CharField(verbose_name=u'max',max_length=50, blank = True, null = True)
    entry = models.CharField(verbose_name=u'entry',max_length=50, blank = True, null = True)
    fileName = models.CharField(verbose_name=u'fileName',max_length=50, blank = True, null = True)
    index = models.CharField(verbose_name=u'index',max_length=50, blank = True, null = True)
    display = models.CharField(verbose_name=u'display',max_length=50, blank = True, null = True)
    displayType = models.CharField(verbose_name=u'displayType',max_length=50, blank = True, null = True)
    add = models.CharField(verbose_name=u'add',max_length=50, blank = True, null = True)
    remove = models.CharField(verbose_name=u'remove',max_length=50, blank = True, null = True)
    update = models.CharField(verbose_name=u'update',max_length=50, blank = True, null = True)
    DomainModel = models.ForeignKey('DomainModel')
    def __unicode__(self):
        return self.code

class Neighbor(models.Model):
    code = models.CharField(verbose_name=u'code',max_length=50)
    extension = models.CharField(verbose_name=u'extension',max_length=50, blank = True, null = True)
    extensionNeighbor = models.CharField(verbose_name=u'extensionNeighbor',max_length=50, blank = True, null = True)
    destinationConcept = models.CharField(verbose_name=u'destinationConcept',max_length=50, blank = True, null = True)
    inverseNeighbor = models.CharField(verbose_name=u'inverseNeighbor',max_length=50, blank = True, null = True)
    internal = models.CharField(verbose_name=u'internal',max_length=50, blank = True, null = True)
    partOfM2M = models.CharField(verbose_name=u'partOfM2M',max_length=50, blank = True, null = True)
    type = models.CharField(verbose_name=u'type',max_length=50, blank = True, null = True)
    min = models.CharField(verbose_name=u'min',max_length=50, blank = True, null = True)
    max = models.CharField(verbose_name=u'max',max_length=50, blank = True, null = True)
    unique = models.CharField(verbose_name=u'unique',max_length=50, blank = True, null = True)
    index = models.CharField(verbose_name=u'index',max_length=50, blank = True, null = True)
    addRule = models.CharField(verbose_name=u'addRule',max_length=50, blank = True, null = True)
    removeRule = models.CharField(verbose_name=u'removeRule',max_length=50, blank = True, null = True)
    UpdateRule = models.CharField(verbose_name=u'UpdateRule',max_length=50, blank = True, null = True)
    display = models.CharField(verbose_name=u'display',max_length=50, blank = True, null = True)
    update = models.CharField(verbose_name=u'update',max_length=50, blank = True, null = True)
    absorb = models.CharField(verbose_name=u'absorb',max_length=50, blank = True, null = True)
    Concept = models.ForeignKey('Concept')
    def __unicode__(self):
        return self.code

class PropertyField(models.Model):
    code = models.CharField(verbose_name=u'code',max_length=50)
    extension = models.CharField(verbose_name=u'extension',max_length=50, blank = True, null = True)
    extensionProperty = models.CharField(verbose_name=u'extensionProperty',max_length=50, blank = True, null = True)
    propertyClass = models.CharField(verbose_name=u'propertyClass',max_length=50, blank = True, null = True)
    derived = models.CharField(verbose_name=u'derived',max_length=50, blank = True, null = True)
    validateType = models.CharField(verbose_name=u'validateType',max_length=50, blank = True, null = True)
    maxLength = models.CharField(verbose_name=u'maxLength',max_length=50, blank = True, null = True)
    required = models.CharField(verbose_name=u'required',max_length=50, blank = True, null = True)
    sensitive = models.CharField(verbose_name=u'sensitive',max_length=50, blank = True, null = True)
    defaultValue = models.CharField(verbose_name=u'defaultValue',max_length=50, blank = True, null = True)
    autoincrement = models.CharField(verbose_name=u'autoincrement',max_length=50, blank = True, null = True)
    unique = models.CharField(verbose_name=u'unique',max_length=50, blank = True, null = True)
    index = models.CharField(verbose_name=u'index',max_length=50, blank = True, null = True)
    reference = models.CharField(verbose_name=u'reference',max_length=50, blank = True, null = True)
    referenceNeighbor = models.CharField(verbose_name=u'referenceNeighbor',max_length=50, blank = True, null = True)
    display = models.CharField(verbose_name=u'display',max_length=50, blank = True, null = True)
    update = models.CharField(verbose_name=u'update',max_length=50, blank = True, null = True)
    displayLength = models.CharField(verbose_name=u'displayLength',max_length=50, blank = True, null = True)
    essential = models.CharField(verbose_name=u'essential',max_length=50, blank = True, null = True)
    scramble = models.CharField(verbose_name=u'scramble',max_length=50, blank = True, null = True)
    whiteSpaceAllowed = models.CharField(verbose_name=u'whiteSpaceAllowed',max_length=50, blank = True, null = True)
    Concept = models.ForeignKey('Concept')
    def __unicode__(self):
        return self.code


