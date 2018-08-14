## Script (Python) "getFolderContents"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=contentFilter=None,batch=False,b_size=100,full_objects=False
##title=wrapper method around to use catalog to get folder contents

if not contentFilter:
    contentFilter = {
        'portal_type': ['newsletter'],
        'sort_on': 'effective',
        'sort_order': 'descending'
    }

return context.getFolderContents(contentFilter, batch, b_size, full_objects)
