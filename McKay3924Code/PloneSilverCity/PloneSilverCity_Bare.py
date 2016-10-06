# This is an implementation of PloneSilverCity without
# any Zope or Plone code. This is used in the book to demonstrate
# the difference between a Plone and a none Plone class.

from source import generate_html, list_generators

class PloneSilverCity:
    def __init__(self, id):
        self.id = id
        self._raw = ""
        self._raw_as_html = ""
        self._raw_language = None       
        
    def edit(self, language, raw_code, file="", safety_belt=""):
        """ The edit function, that sets
        all our parameters, and turns the code
        into pretty HTML """
        filename = ""
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

    def getLanguage(self):
        """ Returns the language that this code has been lexed with """
        return self._raw_language
                        
    def getLanguages(self):
        """ Returns the list of languages available """
        langs = []
        
        for name, description in list_generators():
            langs.append( {'value':value, 'name':description } )
            
        langs.sort()
        return langs
        
    def getRawCode(self):
        """ Returns the raw code """
        return self._raw
    
    def getHTMLCode(self):
        """ Returns the html code """
        return self._raw_as_html
