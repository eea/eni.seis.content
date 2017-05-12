vocab = context.event_countries_vocab();
res = context.portal_catalog.searchResults(
        portal_type=['News Item'],
        review_state='published',
        sort_on='effective',
        sort_order='descending',
        path='/south/communication/newsletter'
        )
news = [b.getObject() for b in res]
news = [n for n in news if vocab[context.Title()] in (n.countries or [])]
return news
