
from proto.metaDb.models import *

nomApp = 'metaDb'


mConcept = Concept.objets.filter( code = nomConcept , model__pk  = idDomain ) 

idApp  = Concept.objets.filter( code = 'Concept' , model__pk  = idDomain ) 



