from plone import api
from Products.Five.browser import BrowserView
from eni.seis.content.util import EventItem


class HomepageView(BrowserView):
    """ Custom homepage
    """

    def get_events(self):
        catalog = api.portal.get_tool('portal_catalog')
        query = {
            'portal_type': 'Event',
        }
        return [EventItem(brain) for brain in catalog(**query)]
