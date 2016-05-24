from Products.Five.browser import BrowserView
from eni.seis.content.util import portal_absolute_url
from eni.seis.content.util import is_east_website
from eni.seis.content.util import is_south_website


class HomepageView(BrowserView):
    """ Custom homepage
    """

    def is_east_website(self):
        return is_east_website(self.request)

    def is_south_website(self):
        return is_south_website(self.request)


class PortalAbsoluteUrlView(BrowserView):
    """ Portal absolute url
    """
    def __call__(self):
        return portal_absolute_url()
