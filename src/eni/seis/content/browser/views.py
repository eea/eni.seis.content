""" BrowserView Controllers
"""

from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from eni.seis.content.config import ALL_REPORTS_CATEGORIES
from eni.seis.content.config import EAST_COUNTRIES
from eni.seis.content.config import UNECE_INDICATORS_CONTAINER
from eni.seis.content.config import UNECE_INDICATORS_SUBCATEGORIES_VOCAB
from eni.seis.content.config import UNECE_INDICATORS_CATEGORIES
from eni.seis.content.util import is_east_website
from eni.seis.content.util import is_south_website
from eni.seis.content.util import portal_absolute_url
from plone import api
from plone.dexterity.utils import createContentInContainer


class HomepageView(BrowserView):
    """ Custom homepage
    """


class CountriesViewEast(BrowserView):
    """ The view for Countries section (East)
    """

    def get_countries_folders(self):
        """ Return list of countries folders
        """
        folders = self.context.portal_catalog.searchResults(
            portal_type=['Folder'],
            review_state='published',
            sort_on='id',
            path='/east/countries'
        )
        folders = [b.getObject() for b in folders]
        countries = [x for x in folders if x.Title() in EAST_COUNTRIES]
        return countries

    def get_country_visits_pages(self):
        """ Return list of country visits pages
        """
        pages = self.context.portal_catalog.searchResults(
            portal_type=['Document'],
            review_state='published',
            sort_on='id',
            path='/east/countries'
        )
        pages = [b.getObject() for b in pages]
        country_visits_pages = [
            x for x in pages if 'country visits' in x.Title().lower()]
        return country_visits_pages


class CountryViewEast(BrowserView):
    """ The view for a country (East)
    """
    def get_indicators_statistics(self):
        """ Generate content for table in UNECE Environmental Indicators tab
        """

        def percentage(percent, whole):
            return (percent * 100.0) / whole

        def indicators_class(percent):
            """ Return
                0 => percentage-0
                [1, 33] => percentage-25
                [34, 66] => percentage-50
                [67, 99] => percentage-75
                100 => percentage-100
                to be used as green backgrounds
            """
            percent = int(percent)
            if percent == 0:
                return "percentage-0"
            if 1 <= percent <= 33:
                return "percentage-25"
            if 34 <= percent <= 66:
                return "percentage-50"
            if 67 <= percent <= 99:
                return "percentage-75"
            if percent == 100:
                return "percentage-100"

        stats = {}
        categories = self.context.unrestrictedTraverse(
            'indicators_data/get_indicators_categories')()
        for category in categories:
            stats[category] = {
                    'indicators_total': 0,
                    'indicators_with_data': 0,
                    'indicators_percentage': 0,
                    'indicators_class': ""
                }
        indicators = self.context.unrestrictedTraverse(
            'indicators_data/get_indicators')()

        for indicator in indicators:
            stats[indicator.category]['indicators_total'] += 1
            if indicator.has_data():
                stats[indicator.category]['indicators_with_data'] += 1

        for category in categories:
            stats[category]['indicators_percentage'] = percentage(
                 stats[category]['indicators_with_data'],
                 stats[category]['indicators_total']
            )
            stats[category]['indicators_class'] = indicators_class(
                 stats[category]['indicators_percentage']
            )
        return stats

    def get_publications_pages(self):
        """ Return list of country publications pages
            from Publications folder
        """
        pages = self.context.portal_catalog.searchResults(
            portal_type=['Document'],
            review_state='published',
            sort_on='id',
            path=self.context.absolute_url_path() + "/publications"
        )
        pages = [b.getObject() for b in pages]
        return pages

    def getLocalNews(self):
        """ Return local news for this country
        """
        vocab = self.context.event_countries_vocab()
        res = self.context.portal_catalog.searchResults(
            portal_type=['News Item'],
            review_state='published',
            sort_on='effective',
            sort_order='descending',
            path='/east/areas-of-work/communication/newsletter'
        )
        news = [b.getObject() for b in res]

        country_title = self.context.Title()
        news = [
            n for n in news if vocab[country_title] in (n.countries or [])]

        return news


class ReportsDataView(BrowserView):
    """ Utils for Reports
    """
    utils = {
        'get_reports_categories()':
            "Return possible categories for a report",
        'get_reports()':
            "Return all published reports found in this context"
    }

    def get_reports_categories(self):
        """ Return possible categories for a report
        """
        return ALL_REPORTS_CATEGORIES

    def get_reports(self):
        """ Return all published reports found in this context
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        results = [x.getObject() for x in catalog.searchResults(
            {
                'portal_type': ['report'],
                'review_state': 'published',
                'path': '/'.join(self.context.getPhysicalPath())
            }
        )]

        return results

    def __call__(self):
        return self.utils


class ReportView(BrowserView):
    """ Report
    """


class IndicatorsDataView(BrowserView):
    """ Utils for Indicators
    """
    utils = {
        'get_indicators_categories()':
            "Return possible categories for an indicator",
        'get_indicators()':
            "Return all published indicators found in this context"
    }

    def get_indicators_categories(self):
        """ Return possible categories for an indicator
        """
        return UNECE_INDICATORS_CATEGORIES

    def get_indicators(self):
        """ Return all published indicators found in this context
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        results = [x.getObject() for x in catalog.searchResults(
            {
                'portal_type': ['indicator'],
                'review_state': 'published',
                'path': '/'.join(self.context.getPhysicalPath())
            }
        )]

        return results

    def __call__(self):
        return self.utils


class IndicatorView(BrowserView):
    """ Indicator
    """


class UpgradeGenerateIndicatorsViewEast(BrowserView):
    """ /upgrade_generate_indicators_east to be unsed in a country section
        to create Indicators folder with all UNECE indicators A1, A2, ...
    """
    def __call__(self):
        country = self.context
        if country.title not in EAST_COUNTRIES:
            return "Nothing changed. Use this upgrade for an East country: " \
                + ", ".join(EAST_COUNTRIES) + "."

        if country.aq_parent.title != "Countries":
            return "Nothing changed. Use this upgrade for an East country: " \
                + ", ".join(EAST_COUNTRIES) + ". (Parent folder: Countries)."

        try:
            indicators_container = country.unrestrictedTraverse(
                UNECE_INDICATORS_CONTAINER[0])
        except AttributeError:
            indicators_container = api.content.create(
                container=country, type='Folder',
                title=UNECE_INDICATORS_CONTAINER[1])
            api.content.transition(obj=indicators_container,
                                   transition='publish')

        for indicator in UNECE_INDICATORS_SUBCATEGORIES_VOCAB:
            # A1, A2, ... => the category is A
            category = ''.join(
                    [i for i in indicator.value if not i.isdigit()])

            item = createContentInContainer(
                indicators_container, "indicator",
                title=indicator.title, category=category,
                subcategory=indicator.value
            )
            api.content.transition(obj=item, transition='publish')

        return "Done. Please verify indicators folder and its contents."


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
