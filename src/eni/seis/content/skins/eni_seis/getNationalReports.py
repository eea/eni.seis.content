res = context.portal_catalog.searchResults(
        portal_type=['nationalreport'],
        review_state='published',
        path='/east/countries'
        )

res = [x.getObject() for x in res]
return res
