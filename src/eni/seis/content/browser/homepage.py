from plone import api
from Products.Five.browser import BrowserView


class HomepageView(BrowserView):
    """ Custom homepage
    """

    def get_events(self):
        catalog = api.portal.get_tool('portal_catalog')
        query = {
            'portal_type': 'Event',
        }
        return [x.getObject() for x in catalog(**query)]
