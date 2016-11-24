##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain

if brain.Type == "EEA Meeting":
    return brain.getObject().meeting_type

return brain.Subject and brain.Subject[0] or ''

