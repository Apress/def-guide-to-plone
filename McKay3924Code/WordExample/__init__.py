from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory

from config import ADD_CONTENT_PERMISSION, PROJECT_NAME

registerDirectory("skins", globals())

def initialize(context):
    ##Import Types here to register them
    import Word

    content_types, constructors, ftis = process_types(
        listTypes(PROJECT_NAME),
        PROJECT_NAME)

    init = utils.ContentInit(
        PROJECT_NAME + ' Content',
        content_types      = content_types,
        permission         = ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        )
    init.initialize(context)
