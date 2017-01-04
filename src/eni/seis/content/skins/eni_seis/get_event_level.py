##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain=None,event=None
##title=Get event level


levels = {
    'Regional Level': 'regional',
    'National Level': 'national',
}

if brain is not None:
    if brain.Type != 'Event':
        return ''

    obj = brain.getObject()

    try:
        event_level = obj.event_level
    except:
        event_level = ''
    return levels.get(event_level, '')

else:
    if event is not None:
        if event.portal_type == 'Event':
            return event.event_level
        else:
            return ''

return ""
