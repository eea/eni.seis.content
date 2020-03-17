res = context.portal_catalog.searchResults(
        portal_type=['productitem'],
        review_state='published',
        path='/east/areas-of-work/access-to-environmental-information/products'
        )

res = [x.getObject() for x in res]
return res
