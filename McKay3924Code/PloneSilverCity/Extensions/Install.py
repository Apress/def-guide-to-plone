from Products.CMFCore.DirectoryView import createDirectoryView
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.TypesTool import FactoryTypeInformation as fti_klass

from Products.PloneSilverCity.config import plone_product_name, product_name
from Products.PloneSilverCity.config import layer_name, layer_location

def install(self):
    """ Install this product """
    out = []
    typesTool = getToolByName(self, 'portal_types')
    skinsTool = getToolByName(self, 'portal_skins')
        
    if id not in typesTool.objectIds():
       typesTool.manage_addTypeInformation(
           fti_klass.meta_type,
           id = plone_product_name,
           typeinfo_name = "%s: %s" % (product_name, product_name)
           )
       out.append('Registered with the types tool')
    else:
       out.append('Object "%s" already existed in the types tool' % (id))

    # add in the directory view pointing to our skin
    if layer_name not in skinsTool.objectIds():
        createDirectoryView(skinsTool, layer_location, layer_name)
        out.append('Added "%s" directory view to portal_skins' % layer_name)

    # add in the layer to all our skins    
    skins = skinsTool.getSkinSelections()
    for skin in skins:
        path = skinsTool.getSkinPath(skin)
        path = [ p.strip() for p in path.split(',') ]
        if layer_name not in path:
            path.insert(path.index('custom')+1, layer_name)

            path = ", ".join(path)
            skinsTool.addSkinSelection(skin, path)
            out.append('Added "%s" to "%s" skins' % (layer_name, skin))
        else:
            out.append('Skipping "%s" skin' % skin)

    return "\n".join(out)
