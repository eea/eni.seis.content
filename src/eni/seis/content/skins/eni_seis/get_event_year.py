##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=contentFilter=None,batch=False,b_size=100,full_objects=False
##title=brain
# retrieves the year from an brain representing an event

start = brain.start

if start:
    return start.year()

return ""

