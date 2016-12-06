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
