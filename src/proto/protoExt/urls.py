from django.conf.urls.defaults import patterns, include, url
#from views import *

from protoMenu import protoGetMenuData
from protoConcept import protoGetPCI, protoGetList


urlpatterns = patterns('', 
    url('protoList.action/$', protoGetList, name='list'),
#    url('create.action/$', create, name='create'),
#    url('update.action/$', update, name='update'),
#    url('delete.action/$', delete, name='delete'),

    url('protoGetMenuData/$', protoGetMenuData ), 
    url('protoGetPCI/$', protoGetPCI ), 

)