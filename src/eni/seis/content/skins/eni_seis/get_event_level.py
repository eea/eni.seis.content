##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain=None,event=None
##title=Get event level


DEFAULT_LEVEL = 'other'

if not brain:
    return DEFAULT_LEVEL

levels = {
    'Regional Level': 'regional',
    'National Level': 'national',
    'Other': 'other',
    'regional': 'regional',
    'national': 'national'
}

if brain.Type not in ['Event', 'Folderish Event', 'EEA Meeting']:
    return DEFAULT_LEVEL

obj = brain.getObject()
try:
    event_level = obj.event_level
except:
    try:
        event_level = obj.meeting_level
    except:
        event_level = DEFAULT_LEVEL
return levels.get(event_level, DEFAULT_LEVEL)
