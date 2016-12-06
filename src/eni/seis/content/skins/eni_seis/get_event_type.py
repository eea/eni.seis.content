if brain.Type == "EEA Meeting":
    return brain.getObject().meeting_type

return brain.Subject and brain.Subject[0] or ''
