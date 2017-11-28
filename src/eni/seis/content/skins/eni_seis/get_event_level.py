##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=brain=None,event=None
##title=Get event level


DEFAULT_LEVEL = 'other'

levels = {
    'Regional Level': 'regional',
    'National Level': 'national',
    'Other': 'other',
    'regional': 'regional',
    'national': 'national'
}

if event is not None:
    obj = event
elif brain is not None:
    obj = brain.getObject()
else:
    return DEFAULT_LEVEL

if obj.portal_type not in ['Event', 'Folderish Event', 'EEA Meeting',
                           'eea.meeting']:
    return DEFAULT_LEVEL

try:
    event_level = obj.event_level
except:
    try:
        event_level = obj.meeting_level
    except:
        event_level = DEFAULT_LEVEL
return levels.get(event_level, DEFAULT_LEVEL)
