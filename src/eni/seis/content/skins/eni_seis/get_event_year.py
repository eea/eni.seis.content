##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain=None,event=None
##title=Retrieves the year from an brain representing an event

if brain:
    start = brain.start
else:
    start = event.start()

if start:
    return start.year()

return ""
