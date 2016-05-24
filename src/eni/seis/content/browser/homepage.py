from Products.Five.browser import BrowserView
from eni.seis.content.util import portal_absolute_url
from eni.seis.content.util import is_east_website
from eni.seis.content.util import is_south_website


class HomepageView(BrowserView):
    """ Custom homepage
    """

    def all_events_url(self):
        return portal_absolute_url() + "/events"

    def event_calendar_url(self):
        return portal_absolute_url() + "/media/events-calendar"

    def section_url(self, abbrev):
        urls = {
            "ma": "/governance/management-group",
            "st_south": "/governance/steering-committee",
            "st_east": "/governance/steering",
            "nf": "/governance/nfps",
            "pr": "/governance/project-reports",
            "ac": "/workplan/activities",
            "me": "/workplan/meetings",
            "re": "/workplan/regional",
        }
        return portal_absolute_url() + urls.get(abbrev, "")

    def is_east_website(self):
        return is_east_website(self.request)

    def is_south_website(self):
        return is_south_website(self.request)
