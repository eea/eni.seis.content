vocab = context.event_countries_vocab()
res = context.portal_catalog.searchResults(
        portal_type=['News Item'],
        review_state='published',
        sort_on='effective',
        sort_order='descending',
        path='/south/communication/newsletter'
        )
news = [b.getObject() for b in res]

here_is_country = context.Title() in vocab;
parents = context.aq_inner.aq_parent.absolute_url().split('/')[3:]
parents_paths = [
    '/' + '/'.join(parents[0:x+1]) + '/' for x in range(0, len(parents))]
find_parent_country_title = [
    context.restrictedTraverse(x).Title() for x in parents_paths if
    context.restrictedTraverse(x).Title() in vocab]
a_parent_country_title = find_parent_country_title[0] if len(
    find_parent_country_title) > 0 else None
country_title = context.Title() if here_is_country else a_parent_country_title
news = [
    n for n in news if vocab[country_title] in (n.countries or [])] if \
    country_title is not None else news

return news
