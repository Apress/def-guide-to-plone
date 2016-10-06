#!/usr/bin/python
#$Id: PersonSQL.py,v 1.2 2004/06/07 20:08:48 andy Exp $
#Copyright: ClearWind Consulting Ltd
#License: http://www.clearwind.ca/license

from Products.Archetypes.public import Schema
from Products.Archetypes.public import IntegerField, StringField
from Products.Archetypes.public import IntegerWidget, StringField
from Products.Archetypes.SQLStorage import PostgreSQLStorage
from config import PROJECT_NAME

schema = BaseSchema + Schema((
    
  IntegerField('age', 
      validators=(("isInt",)),
      storage = SQLStorage(),
      widget=IntegerWidget(label="Your age"),

      ),

  StringField('email',
      validators = ('isEmail',),
      index = "TextIndex",
      storage = SQLStorage(),
      widget = StringWidget(label='Email',)
      ),
    
    ))

class PersonSQL(BaseContent):
    """Our person object"""
    schema = schema
                  
registerType(PersonSQL, PROJECT_NAME)