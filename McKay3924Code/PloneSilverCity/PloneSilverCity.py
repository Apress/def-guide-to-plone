# $Id: PloneSilverCity.py,v 1.5 2004/03/02 03:46:21 zopezen Exp $
# Copyright: ClearWind Consulting Ltd

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.CMFDefault.DublinCore import DefaultDublinCoreImpl
from Products.CMFCore.PortalContent import PortalContent

from webdav.Lockable import ResourceLockedError

from config import product_name, plone_product_name
from config import add_permission, edit_permission, view_permission
from source import generate_html, list_generators

factory_type_information = {
     'id': plone_product_name,
     'meta_type': product_name,
     'description': ('Provides syntax highlighted HTML of source code.'),
     'product': product_name,
     'factory': 'addPloneSilverCity',
     'content_icon': 'silvercity.gif',
     'immediate_view': 'view',
     'actions': (
                 {'id': 'view',
                  'name': 'View',
                  'action': 'silvercity_view',
                  'permissions': (view_permission,)},
                 {'id': 'source',
                  'name': 'Source',
                  'action': 'getRawCode',
                  'permissions': (view_permission,)},
                 {'id': 'edit',
                  'name': 'Edit',
                  'action': 'silvercity_edit_form',
                  'permissions': (edit_permission,)},
                 ),
     }

def addPloneSilverCity(self, id, REQUEST=None):
    """ This is our factory function and creates
    an empty PloneSilverCity object inside our Plone
    site """
    obj = PloneSilverCity(id)
    self._setObject(id, obj)

class PloneSilverCity(PortalContent, DefaultDublinCoreImpl):
    meta_type = product_name
    
    __implements__ = ( 
        PortalContent.__implements__,
        DefaultDublinCoreImpl.__implements__
        )
                         
    security = ClassSecurityInfo()
    
    def __init__(self, id):
        DefaultDublinCoreImpl.__init__(self)
        self.id = id
        self._raw = ""
        self._raw_as_html = ""
        self._raw_language = None
 
    security.declareProtected(edit_permission, "edit")
    def edit(self, language, raw_code, file="", safety_belt=""):
        """ The edit function, that sets
        all our parameters, and turns the code
        into pretty HTML """
        filename = ""

        if not language:
            language = self.getLanguage()
            
        if file:
            file_code = file.read()
        
            # if there is a file, and we've read it and its not blank...
            if file_code:
                raw_code = file_code
                if hasattr(file, "name"):
                    filename = file.name
                else:
                    filename = file.filename
                # set the language to None so it will be set by SilverCity                
                language = None
        
        self._raw = raw_code
                
        # our function, generate_html does the hard work here
        html, language = generate_html(raw_code, language, filename)
        self._raw_as_html = html
        self._raw_language = language

    security.declareProtected(view_permission, "getLanguage")
    def getLanguage(self):
        """ Returns the language that this code has been lexed with """
        return self._raw_language
                        
    security.declareProtected(view_permission, "getLanguages")        
    def getLanguages(self):
        """ Returns the list of languages available """
        langs = []
     
        for value, description in list_generators():
            langs.append( {'value':value, 'name':description } )
            
        langs.sort()
        return langs
        
    security.declareProtected(view_permission, "getRawCode")
    def getRawCode(self):
        """ Returns the raw code """
        return self._raw
    
    security.declareProtected(view_permission, "getHTMLCode")
    def getHTMLCode(self):
        """ Returns the html code """
        return self._raw_as_html

    security.declareProtected(view_permission, "SearchableText")
    def SearchableText(self):
        """ Used by the catalog for basic full text indexing """
        return "%s %s %s" % ( self.Title()
                            , self.Description()
                            , self._raw
                            )
    
    # This is support for FTP and ExternalEditor
    # these are optional, but ExternalEditor is extremely
    # useful
    
    security.declareProtected(view_permission, 'manage_FTPget')
    def manage_FTPget(self):
        """ For FTP and ExternalEditor support """
        return self.getRawCode()
           
    security.declareProtected(edit_permission, 'PUT')
    def PUT(self, REQUEST, RESPONSE):
        """ Handle HTTP PUT requests, for incoming FTP """
        self.dav__init(REQUEST, RESPONSE)
        self.dav__simpleifhandler(REQUEST, RESPONSE, refresh=1)
        body = REQUEST.get('BODY', '')

        try:
            self.edit(language=None, raw_code=body)
        except ResourceLockedError, msg:
            get_transaction().abort()
            RESPONSE.setStatus(423)
            return RESPONSE

        RESPONSE.setStatus(204)
        self.reindexObject()
        return RESPONSE
  
InitializeClass(PloneSilverCity)
