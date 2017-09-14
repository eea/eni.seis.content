nfps = [
    b.getObject() for b in context.portal_catalog.searchResults(
            portal_type=['nfp'],
            review_state='published',
            sort_on='getObjPositionInParent',
            path='/'.join(context.getPhysicalPath())
        )
    ]

return nfps
