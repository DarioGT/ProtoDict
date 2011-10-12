# The core system of my application

# Import XML module
from xml.etree.ElementTree import ElementTree
import xml.parsers.expat as expat
import xml.etree.ElementTree as Xml

# Conf Django 
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'proto.settings'

from django.core import management
import proto.settings as settings 
management.setup_environ(settings)


# Import the logger
import logging

#Import Database class
from proto.metaDb.models import *  

class importXML():
    def __init__(self):
        self.__filename = ""
        self.__tree = None
        self.__session = None

        
        self.__logger = logging.getLogger("Convert XML Database")
        self.__logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)
        
        
        # Errors Constants
        self.OK = 0
        self.ERROR_OPEN_FILE = 1
        self.ERR0R_PARSE_XML = 2
        self.OPERATIONAL_ERROR = 3
        self.ADDING_ERROR = 4
        self.ERROR = 5
        
    # PRECONDITIONS : filename doit etre un fichier XML
    def loadFile(self, filename):
        # In oder to conserve the file
        self.__tree = ElementTree()
        
        #Logging info
        self.__logger.info("Chargement du fichier...")
        
        #self.__tree.parse(filename)
        try:
            self.__tree.parse(filename)
            self.__filename = filename
            
        except IOError:
            self.__logger.critical("Impossible d ouvrir le fichier...")
            return self.ERROR_OPEN_FILE
        except expat.ExpatError:
            self.__logger.critical("Erreur de parsage du fichier...")
            return self.ERR0R_PARSE_XML
        except:
            self.__logger.critical("Erreur de traitement fichier...")
            return self.ERROR
        
        #Logging info
        self.__logger.info("Chargement du fichier effectue...")
        
        return self.OK
        
        
    #RETOUR : le nom d un fichier XML
    def getFilename(self):
        return self.__filename
    
    # Transform XML Element  to text
    def getContentFile(self):
        
        #Logging info
        self.__logger.info("Obtention du contenu du fichier...")
        
        contenu = None
        if (self.__tree == None):
            contenu = ""
        else:
            contenu = Xml.tostring(self.__tree.getroot())
            
        #Logging info
        self.__logger.info("Obtention du contenu du fichier effectuee...")    
        return contenu
    
        
    def __write(self):

        #Logging info
        self.__logger.info("Ecriture dans la base de donnee...")

        #Listas 
        fdsDomain = [field.name for field in Domain._meta.fields]
        
        fdsModel= [field.name for field in Model._meta.fields]
        fdcModel = [("idModel", "modelIx"),("idref","modelRef") ]
        
        fdsConcept= [field.name for field in Concept._meta.fields]
        fdsProperty= [field.name for field in Property._meta.fields]
        fdsNeighbor= [field.name for field in Relationship._meta.fields]

        #Temp var 
        field = None
        
        # We populate the database
#       try: 
        if (self.__tree != None):  # A file has been loaded
        
            xDomains = self.__tree.getiterator("domain")
            
            for xDomain in xDomains:
                lDomain = Domain()
                for child in xDomain:
                    if child.tag in fdsDomain:
                        setattr( lDomain, child.tag, child.text ) 
                    else: 
                        pass 
                        
                lDomain.save()
                self.__logger.info("Domain..."  + lDomain.code)

                
                xModels = xDomain.getiterator("model")
                for xModel in xModels:
                    dModel = Model()
                    dModel.domain = lDomain

                    for child in xModel:
                        if child.tag in fdsModel:
                            setattr( dModel, child.tag, child.text ) 
                    dModel.save()
                    self.__logger.info("Model..."  + dModel.code)

                    xConcepts = xModel.getiterator("concept")
                    for xConcept in xConcepts:
                        concept = Concept()
                        concept.model = dModel
                        
                        for child in xConcept:
                            if child.tag in fdsConcept:
                                setattr( concept, child.tag, child.text ) 
                        concept.save()
                        self.__logger.info("Concept..."  + concept.code)

                        xPropertys = xConcept.getiterator("property")
                        for xProperty in xPropertys:
                            lProperty = Property()
                            lProperty.concept = concept

                            for child in xProperty:
                                if child.tag in fdsProperty:
                                    setattr( lProperty, child.tag, child.text )
                            lProperty.save()

                        xNeighbors = xConcept.getiterator("foreign")
                        for xNeighbor in xNeighbors:
                            foreign = Relationship()
                            foreign.concept = concept
                            
                            for child in xNeighbor:
                                if child.tag in fdsNeighbor:
                                    setattr( foreign, child.tag, child.text )
                            foreign.save()


#        except KeyError, e:
#            #Logging critical
#            self.__logger.critical("Erreur d attribut.")
#            return {'state':self.ADDING_ERROR, 'message': 'Erreur attribut :'+str(e)} 
#                         
#        except Exception, e:
#            #Logging critical
#            self.__logger.critical("Impossible d ecrire dans la base de donnee.")
#            return {'state':self.ADDING_ERROR, 'message': str(e)} 
        
        #Logging info
        self.__logger.info("Ecriture dans la base de donnee effectuee...")
        
        return {'state':self.OK, 'message': 'Ecriture effectuee'}
    
    def writeDatabase(self): 
        # We write in the database
        dictWrite = self.__write()
        if (dictWrite['state'] != self.OK):
            return dictWrite
                
        return {'state':self.OK, 'message': 'Ecriture effectuee base donnee'}
    
