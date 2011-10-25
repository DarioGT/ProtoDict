# -*- encoding: UTF-8 -*-
#
import sys

from django.db import models

from django.contrib.auth.models import User
from django import forms
             

from django.http import HttpResponse, HttpResponseRedirect
from django.template import  Context
from django.template import  RequestContext
from django.template.loader import get_template 

from protoExtJs import protoGrid, utils 
from protoExtJs.forms import ExtJsForm, getExtJsModelForm

def getDjangoModel( modelName ):
    # Encuentra el modelo 
    for m in models.get_models():
        if m._meta.object_name.lower() == modelName.lower():
            model = m
            break

    return model 



# Create your views here.
def protoGridDefinition(request):
    # used like this in the main urls.py :
    #(r'^apps/(?P<app>[^/]+)/(?P<view>[^/]+)$', 'core.appdispatcher.dispatch' ), --> apps/app/views.py/view
    #(r'^apps/(?P<app>[^/]+)/?$', 'core.appdispatcher.dispatch' ),               --> apps/app/views.py/default
    

    modelName, value  = request.GET.items()[0]
    model = getDjangoModel(modelName)

    # Define la grilla con base en el modelo 
    grid = protoGrid.ProtoGridFactory( model )        # generic from model fields

    
    # if you have an EditableModelGrid then you can use POST data to update your instances.
    if request.method == 'POST':

        # handle save of grid data !
        if request.POST.get('delete', '')!='':

            modelName = request.GET.items()[0]

            dels = request.POST['delete'].split(',')
            User.objects.filter(id__in = dels).delete()
            return utils.JsonSuccess()
            # delete selected rows
        if request.POST.get('update', '')!='':    
            # update rows data (update+inserts)
            if 1: #try:
                grid.update_instances_from_json(request.POST['update'])
                return utils.JsonSuccess()
            else: #except:
                #print "Unexpected error:", sys.exc_info()[0]
                msg = getattr(sys.exc_info()[1], 'message', sys.exc_info()[0])
                #.message
                return utils.JsonError(str(msg))


    # Obtiene las filas del modelo 
    pRows = model.objects.all()
    
    # parametros de trabajo 
    start = request.POST.get('start', 0)
    limit = request.POST.get('limit', 20)
    sort = request.POST.get('sort', 'id')
    sort_dir = request.POST.get('dir', 'ASC')
    json = grid.to_grid(
                            pRows, 
                            start = start, 
                            limit =  limit, 
                            totalcount = pRows.count(), 
                            sort_field = sort, 
                            sort_direction = sort_dir
                            )

    resp = utils.JsonResponse(json)
    return resp


#class BaseCustomGridUsers(object):
#    class Meta:
#        exclude = []
#        order = ['id', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']
#        fields_conf = {}
#        fields_conf['id'] = {'hidden':True, 'width':30, 'align':'center'}
#        fields_conf['date_joined'] = {'type':'date', 'header':u'date_joined', 'width':90,  'dateFormat':'d/m/Y', 'renderer':"new Ext.util.Format.dateRenderer('d/m/Y')", 'align':'center'}
#        fields_conf['is_staff'] = {'width':50, 'header':'staff', 'align':'center', 'renderer':"function(val, attr) {attr.css = (val)?'icon-accept':'icon-delete'; }"}
#        fields_conf['is_active'] = {'width':50, 'header':'active', 'align':'center', 'renderer':"function(val, attr) {attr.css = (val)?'icon-accept':'icon-delete'; }"}
#        fields_conf['is_superuser'] = {'width':50, 'header':'root', 'align':'center', 'renderer':"function(val, attr) {attr.css = (val)?'icon-accept':'icon-delete'; }"}
#
#        
## this is the same as above
#class CustomGridUsers(BaseCustomGridUsers, grids.ModelGrid):
#    pass
#        
## the same but editable !
#class CustomEditableGridUsers(BaseCustomGridUsers, grids.EditableModelGrid):
#    pass
#    
##
## Simple contact form example
##
#
#class ContactForm(forms.Form):
#    name = forms.CharField(label='your name')
#    phone = forms.CharField(label='phone number', required = False)
#    mobile_type = forms.CharField(label='phone type', required = True)
#    mobile_type.choices = [
#         ('ANDROID','Android')
#        ,('IPHONE','iPhone')
#        ,('SYMBIAN','Symbian (nokia)')
#        ,('OTHERS','Others')
#    ]
#    email = forms.EmailField(label='your email', initial='test@revolunet.com')
#    message = forms.CharField(label='your message', widget = forms.widgets.Textarea(attrs={'cols':15, 'rows':5}))
#
#ExtJsForm.addto(ContactForm)
#        
#@publish
#def contact_form(request, path = None):
#    if request.method == 'POST':
#        # handle form submission
#        form = ContactForm(request.POST)
#        if not form.is_valid():
#            return utils.JsonError(form.html_errorlist())
#        else:
#            # send your email
#            print 'send a mail'
#            
#        return utils.JsonResponse("{success:true, messages: [{icon:'/core/static/img/famfamfam/accept.png', message:'Enregistrement OK'}]}" )
#    else:
#        # handle form display
#        form = ContactForm()
#        return utils.JsonResponse(utils.JSONserialise(form.as_extjsfields()))
#        
#        
##
## Generic ModelForm Example
##
#
#class UserForm(forms.ModelForm):
#    class Meta:
#        exclude = ['groups', 'user_permissions', 'password']
#        model = User
#    def __init__(self, *args, **kwargs):
#        super(UserForm, self).__init__(*args, **kwargs)
#        if self.instance:
#            self.fields['pk'] = forms.CharField(initial = self.instance.pk, widget=forms.widgets.HiddenInput)
#            
#ExtJsForm.addto(UserForm)
#
#@publish
#def user_edit(request, path = None):
#    if request.method == 'POST':
#        # handle form submission
#        data = request.POST.copy()
#        user = User()        
#        if request.POST.get('pk','')!='':
#            user = User.objects.get(pk = request.POST['pk'])
#        else:
#            data['pk']=0    # force new ID if no pk given
#            
#        form = UserForm(data)
#        form.instance = user
#        if not form.is_valid():
#            print form.html_errorlist()
#            return utils.JsonError(form.html_errorlist())
#        form.save()
#        return utils.JsonResponse("{success:true, messages: [{icon:'/core/static/img/famfamfam/accept.png', message:'Enregistrement OK'}]}" )
#    else:
#        # handle form display
#        user = User()
#        if request.GET.get('pk','')!='':
#            user = User.objects.get(pk = request.GET['pk'])
#        form = UserForm(instance = user)
#        
#        formExtjs = form.as_extjsfields()
#        
#        return utils.JsonResponse(utils.JSONserialise(formExtjs))
# 

#@publish
#def customer_edit(request):
#    
#    formclass = getExtJsModelForm(models.Customer)
#    #ExtJsForm.addto(formclass)
#    form = formclass()
#    if request.method == 'POST':
#        id = request.POST.get('id', None)
#        instance = models.Customer()
#        if id:
#            instance = models.Customer.objects.get(id = id)
#            
#        form = formclass(request.POST, instance = instance)
#        if not form.is_valid():
#            print form.html_errorlist()
#            return utils.JsonError(form.html_errorlist())
#        else:
#            form.save()
#            return utils.JsonSuccess()
#    
#    # hide django auto-added first combo items ('------')
##    form.fields['gender'].choices = form.fields['gender'].choices[1:]
##    form.fields['ctype'].choices = form.fields['ctype'].choices[1:]
#    
#    return utils.JsonResponse(utils.JSONserialise(form.as_extjsfields()))
#    
#    
#class CustomerEditableGrid(grids.EditableModelGrid):
#    def __init__(self, *args, **kwargs):
#        super(CustomerEditableGrid, self).__init__(*args, **kwargs)
#        #self.get_field('last_datetime').update({'width':150})
#    class Meta:
#        exclude = ['date','datetime']
#        
