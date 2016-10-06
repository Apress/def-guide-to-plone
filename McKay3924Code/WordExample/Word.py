from Products.Archetypes.public import BaseSchema, Schema
from Products.Archetypes.public import TextField
from Products.Archetypes.public import RichWidget
from Products.Archetypes.public import BaseContent, registerType
from Products.Archetypes.Marshall import PrimaryFieldMarshaller
from Products.CMFCore import CMFCorePermissions
from config import PROJECT_NAME

schema = BaseSchema +  Schema((
    TextField('body',
              searchable=1,
              required=1,
              primary=1,
              default_output_type='text/html',
              allowable_content_types=('application/msword',),
              widget=RichWidget(label='Body'),
              ),
    ),
    marshall=PrimaryFieldMarshaller(),
    )

class WordExample(BaseContent):
    """This is a sample article, it has an overridden view for show,
    but this is purely optional
    """
    content_icon = "word_icon.gif"
    schema = schema

registerType(WordExample, PROJECT_NAME)
