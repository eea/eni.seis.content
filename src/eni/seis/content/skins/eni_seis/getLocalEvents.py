vocab = context.event_countries_vocab()

events = [
        b.getObject() for b in context.portal_catalog.searchResults(
            portal_type=['Event', 'eea.meeting'],
            review_state='published',
            sort_on='start',
            sort_order='reverse')
        ]

events = [ev
    for ev in events
    if vocab[context.Title()] in (ev.countries or [])
]

return events
