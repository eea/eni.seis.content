if brain.Type == 'EEA Meeting':
    obj = brain.getObject()
    return obj.location
    return obj.absolute_url()

return brain.location
