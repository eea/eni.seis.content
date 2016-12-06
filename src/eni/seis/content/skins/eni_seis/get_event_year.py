# retrieves the year from an brain representing an event

if brain:
    start = brain.start
else:
    start = event.start()

if start:
    return start.year()

return ""
