res = context.portal_catalog.searchResults(
        portal_type=['eea.meeting'],
        review_state='published',
        sort_on='sort',
        sort_order='descending',
        path='/east/areas-of-work/communication/events'
        )
meetings = [b for b in res]
featured = [x for x in meetings if x.getObject().is_featured is True]

regional = []
national = []
for x in featured:
    if context.get_event_level(x) == 'regional':
        regional.append(x)
    elif context.get_event_level(x) == 'national':
        national.append(x)

return regional + national
