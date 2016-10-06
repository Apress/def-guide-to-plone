import PloneSilverCity

from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory

from config import product_name, add_permission

contentConstructors = (PloneSilverCity.addPloneSilverCity,)
contentClasses = (PloneSilverCity.PloneSilverCity,)
contentFTI = (PloneSilverCity.factory_type_information,)

registerDirectory('skins', globals())

def initialize(context):
    product = utils.ContentInit(product_name, 
        content_types = contentClasses,
        permission = add_permission,
        extra_constructors = contentConstructors,
        fti = contentFTI)
    product.initialize(context)
