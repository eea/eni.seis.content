res = context.portal_catalog.searchResults(
        portal_type=['News Item', 'Folderish News Item'],
        review_state='published',
        sort_on='effective',
        sort_order='descending',
        path='/south/communication/news'
        )
news = [b.getObject() for b in res]

return news
