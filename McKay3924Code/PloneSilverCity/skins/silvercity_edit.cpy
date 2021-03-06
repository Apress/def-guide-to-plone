## Controller Python Script "silvercity_edit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=text_format, text, file='', SafetyBelt='', title='', description='', id=''
##title=Edit a document

filename=getattr(file,'filename', '')
if file and filename:
    # if there is no id, use the filename as the id
    if not id:
        id = filename[max( filename.rfind('/')
                       , filename.rfind('\\')
                       , filename.rfind(':') )+1:]
    file.seek(0)

# if there is no id specified, keep the current one
if not id:
    id = context.getId()
    
new_context = context.portal_factory.doCreate(context, id)
new_context.edit( text_format
                , text
                , file
                , safety_belt=SafetyBelt )

from Products.CMFPlone import transaction_note
transaction_note('Edited source code %s at %s' % (new_context.title_or_id(), new_context.absolute_url()))

new_context.plone_utils.contentEdit( new_context
                                   , id=id
                                   , title=title
                                   , description=description )

return state.set(context=new_context, portal_status_message='Source code changes saved.')
