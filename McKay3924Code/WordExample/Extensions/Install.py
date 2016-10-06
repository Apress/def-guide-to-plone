from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.WordExample.config import PROJECT_NAME, GLOBALS

from StringIO import StringIO

def install(self):
    out = StringIO()
    installTypes(self, out, listTypes(PROJECT_NAME), PROJECT_NAME)
    install_subskin(self, out, GLOBALS)
    out.write("Successfully installed %s." % PROJECT_NAME)
    return out.getvalue()
