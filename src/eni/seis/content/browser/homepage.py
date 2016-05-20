from plone import api
from Products.Five.browser import BrowserView
from eni.seis.content.util import EventItem
from eni.seis.content.util import portal_absolute_url


class HomepageView(BrowserView):
    """ Custom homepage
    """

    def get_events(self):
        catalog = api.portal.get_tool('portal_catalog')
        query = {
            'portal_type': 'Event',
            'sort_on': 'start',
            'sort_order': 'ascending'
        }

        return [EventItem(brain) for brain in catalog(**query)]

    def all_events_url(self):
        return portal_absolute_url() + "/events"

    def event_calendar_url(self):
        return portal_absolute_url() + "/media/events-calendar"

    def section_url(self, abbrev):
        urls = {
            "ma": "/governance/management-group",
            "st": "/governance/steering-committee",
            "nf": "/governance/nfps",
            "pr": "/governance/project-reports",
            "ac": "/workplan/activities",
            "me": "/workplan/meetings",
            "re": "/workplan/regional",
        }
        return portal_absolute_url() + urls.get(abbrev, "")
