res = context.portal_catalog.searchResults(
        portal_type=['nationalreport'],
        review_state='published',
        path='/east/countries'
        )

return res
