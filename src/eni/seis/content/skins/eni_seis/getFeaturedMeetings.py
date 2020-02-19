res = context.portal_catalog.searchResults(
        portal_type=['eea.meeting'],
        review_state='published',
        sort_on='sort',
        sort_order='descending',
        path='/east/areas-of-work/communication/events'
        )
meetings = [b.getObject() for b in res]
featured = [x for x in meetings if x.is_featured is True]

return featured
