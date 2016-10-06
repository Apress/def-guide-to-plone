from Products.CMFCore.TypesTool import ContentFactoryMetadata
from Products.CMFCore.DirectoryView import createDirectoryView
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.TypesTool import FactoryTypeInformation as fti_klass

from Products.PloneBookExamples.config import layer_name, layer_location

def install(self):
    """ Install this product """
    out = []
    typesTool = getToolByName(self, 'portal_types')
    skinsTool = getToolByName(self, 'portal_skins')
        
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

# Andy McKay
# June 5th, add this as a convenience to 
# clear out all the skin settings for installing and uninstalling
# this product
def uninstall(self):
    """ UnInstall this product """
    out = []
    typesTool = getToolByName(self, 'portal_types')
    skinsTool = getToolByName(self, 'portal_skins')
        
    # add in the directory view pointing to our skin
    if layer_name in skinsTool.objectIds():
        skinsTool.manage_delObjects([layer_name,])
        out.append('Deleted "%s" directory view from portal_skins' % layer_name)

    # add in the layer to all our skins    
    skins = skinsTool.getSkinSelections()
    for skin in skins:
        path = skinsTool.getSkinPath(skin)
        path = [ p.strip() for p in path.split(',') ]
        if layer_name not in path:
            del path[path.index(layer_name)]

            path = ", ".join(path)
            skinsTool.addSkinSelection(skin, path)
            skinsTool.addSkinSelection(skin, path)
            out.append('Removed "%s" from %s" skins' % (layer_name, skin))
        else:
            out.append('Skipping "%s" skin' % skin)

    return "\n".join(out)
