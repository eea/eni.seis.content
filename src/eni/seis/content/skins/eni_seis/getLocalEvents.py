vocab = context.event_countries_vocab()

events = [
        b.getObject() for b in context.portal_catalog.searchResults(
            portal_type=['Event', 'eea.meeting'],
            review_state='published',
            sort_on='start',
            sort_order='reverse')
        ]

here_is_country = context.Title() in vocab
parents = context.aq_inner.aq_parent.absolute_url().split('/')[3:]
parents_paths = [
    '/' + '/'.join(parents[0:x+1]) + '/' for x in range(0, len(parents))]
find_parent_country_title = [
    context.restrictedTraverse(x).Title() for x in parents_paths if
    context.restrictedTraverse(x).Title() in vocab]
a_parent_country_title = find_parent_country_title[0] if len(
    find_parent_country_title) > 0 else None
country_title = context.Title() if here_is_country else a_parent_country_title
events = [
    ev for ev in events if vocab[country_title] in (ev.countries or [])] if \
    country_title is not None else events

return events
