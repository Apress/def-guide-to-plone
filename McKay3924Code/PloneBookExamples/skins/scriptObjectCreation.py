##title=Create 
##parameters=
# create with a random id
newId = context.generateUniqueId('Folder')

# create a object of type Folder
context.invokeFactory(id=newId, type_name='Folder')
newFolder = getattr(context, newId)

# create a new Document type
newFolder.invokeFactory(id='index.html', type_name='Document')

# get the new page
newPage = getattr(newFolder, 'index.html')
newPage.edit('html', '<p>This is the default page.</p>')

# return something back to the calling script
return "Done"