res = context.portal_catalog.searchResults(
        portal_type=['productitem'],
        review_state='published',
        sort_on='getObjPositionInParent',
        path='/east/areas-of-work/data/land/products'
        )

items = {}
res = [x.getObject() for x in res]
for item in res:
    try:
        category = item.category[0]
    except Exception:
        category = "unlisted"

    if items.get(category, None) is None:
        items[category] = []

    items[category].append(item)

return items
