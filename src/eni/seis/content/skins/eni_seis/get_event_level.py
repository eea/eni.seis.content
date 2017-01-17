##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain=None,event=None
##title=Get event level


if not brain:
    return ''

if brain.Type != 'Event':
    return ''

levels = {
    'Regional Level': 'regional',
    'National Level': 'national',
}

obj = brain.getObject()
try:
    event_level = obj.event_level
except:
    event_level = ''
return levels.get(event_level, '')
