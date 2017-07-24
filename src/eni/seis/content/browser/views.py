""" BrowserView Controllers
"""

from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from eni.seis.content.config import ALL_REPORTS_CATEGORIES
from eni.seis.content.util import is_east_website
from eni.seis.content.util import is_south_website
from eni.seis.content.util import portal_absolute_url


class HomepageView(BrowserView):
    """ Custom homepage
    """


class CountryViewEast(BrowserView):
    """ The view for a country (East)
    """


class ReportsDataView(BrowserView):
    """ Utils for Reports
    """
    utils = {
        'get_all_reports_categories()':
            "Return possible categories for a report",
        'get_all_reports()':
            "Return all published reports found in this context"
    }

    def get_all_reports_categories(self):
        """ Return possible categories for a report
        """
        return ALL_REPORTS_CATEGORIES

    def get_all_reports(self):
        """ Return all published reports found in this context
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        results = [x.getObject() for x in catalog.searchResults(
            {
                'portal_type': ['report'],
                'review_state': 'published'
            }
        )]

        return results

    def __call__(self):
        return self.utils


class ReportView(BrowserView):
    """ Report
    """


class GetUpcomingEventsView(BrowserView):
    """ Next future Event and eea.meetings items list
    """
    def __call__(self):
        now = DateTime()

        events = [
            b.getObject() for b in self.context.portal_catalog.searchResults(
                portal_type=['Event', 'eea.meeting'],
                review_state='published',
                sort_on='start')
            if b.start > now
        ]

        return events


class PortalAbsoluteUrlView(BrowserView):
    """ Portal absolute url
    """
    def __call__(self):
        return portal_absolute_url()


class IsEastWebsiteView(BrowserView):
    """ Return True for EAST website else False
    """
    def __call__(self):
        return is_east_website(self.request)


class IsSouthWebsiteView(BrowserView):
    """ Return True for SOUTH website else False
    """
    def __call__(self):
        return is_south_website(self.request)


class EventsListing(BrowserView):
    """ Custom Listing for Events
    """
    def tabs(self):
        """ Get tabs
        """
        query = {'portal_type': 'Folder'}
        return self.context.getFolderContents(query, full_objects=True)

    def entries(self, tab=None):
        """ Tab entries
        """
        return tab.getFolderEvents()

    def macro(self, tab=None):
        """ Tab macro
        """
        layout = tab.getLayout()
        if not layout:
            layout = 'folder_summary_view'

        view = tab.restrictedTraverse(layout)
        macros = getattr(view, 'macros', {})
        macro = macros.get('listing', None)

        if not macro:
            view = tab.restrictedTraverse('folder_summary_view')
            return view.macros['listing']
        return macro


class SubscriberRoles(BrowserView):
    """ Subscriber Roles List from subscriber_roles vocabulary
    """
    def __call__(self):
        terms = self.context.portal_vocabularies.getVocabularyByName(
            'subscriber_roles').items()
        res = [(t[0], t[1].title) for t in terms]
        return res
