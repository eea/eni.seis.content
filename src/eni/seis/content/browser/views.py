""" BrowserView Controllers
"""

from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from collections import OrderedDict
from datetime import datetime
from eni.seis.content.config import EAST_COUNTRIES
from eni.seis.content.config import EAST_COUNTRIES_DICT
from eni.seis.content.config import REPORTS_CONTAINER
from eni.seis.content.config import REPORTS_TYPES_VOCAB
from eni.seis.content.config import SOUTH_COUNTRIES
from eni.seis.content.config import UNECE_INDICATORS_CATEGORIES
from eni.seis.content.config import UNECE_INDICATORS_CONTAINER
from eni.seis.content.config import UNECE_INDICATORS_SUBCATEGORIES
from eni.seis.content.config import UNECE_INDICATORS_SUBCATEGORIES_VOCAB
from eni.seis.content.util import is_east_website
from eni.seis.content.util import is_south_website
from eni.seis.content.util import portal_absolute_url
from itertools import groupby
from plone import api
from plone.dexterity.utils import createContentInContainer
from zope.annotation.interfaces import IAnnotations


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


def get_indicators_statistics(context):
    """ Generate content for table in UNECE Environmental Indicators tab
    """

    stats = {}
    categories = context.unrestrictedTraverse(
        'indicators_data/get_indicators_categories')()
    for category in categories:
        stats[category] = {
                'indicators_total': 0,
                'indicators_with_data': 0,
                'indicators_percentage': 0,
                'indicators_class': ""
            }
    indicators = context.unrestrictedTraverse(
        'indicators_data/get_indicators')()

    for indicator in indicators:
        stats[indicator.category]['indicators_total'] += 1
        if indicator.has_data():
            stats[indicator.category]['indicators_with_data'] += 1

    total_value = 0
    for category in categories:
        stats[category]['indicators_percentage'] = percentage(
             stats[category]['indicators_with_data'],
             stats[category]['indicators_total']
        )
        total_value += stats[category]['indicators_percentage']
        stats[category]['indicators_class'] = indicators_class(
             stats[category]['indicators_percentage']
        )
    total_value_percentage = total_value / len(categories)
    stats['total'] = {
        'indicators_class': indicators_class(total_value_percentage)
    }
    return stats


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
            portal_type=['Document', 'Folderish Document'],
            review_state='published',
            sort_on='getObjPositionInParent',
            path='/east/countries'
        )
        pages = [b.getObject() for b in pages]
        country_visits_pages = [
            x for x in pages if 'country visits' in x.Title().lower()]
        return country_visits_pages

    def get_indicators_table_data(self):
        """ Return data used in UNECE ENVIRONMENTAL INDICATORS table with tabs
        """
        indicators = self.context.unrestrictedTraverse(
            'indicators_data/get_indicators')()

        indicators_data = [
            {
                'country': x.aq_parent.aq_parent.Title(),
                'category': x.category,
                'subcategory': x.subcategory,
                'has_data': x.has_data(),
                'object': x
            } for x in indicators]

        categories = [x for x in UNECE_INDICATORS_CATEGORIES]
        subcategories = [x for x in UNECE_INDICATORS_SUBCATEGORIES]
        countries = EAST_COUNTRIES
        result = {}
        for category in categories:
            result[category] = {}
            for subcategory in subcategories:
                if subcategory[0] == category:  # for A select only A1, A2...
                    result[category][subcategory] = {}
                    for country in countries:
                        result[category][country] = {
                            'indicators_with_data': 0
                        }

        for indicator in indicators_data:
            data_value = 0 if indicator['has_data'] is False else 1
            result[indicator['category']][
                    indicator['subcategory']][indicator['country']] = {
                            'has_data': indicator['has_data'],
                            'object': indicator['object']
                        }
            result[indicator['category']][indicator['country']][
                'indicators_with_data'] += data_value

        return {
            'categories': categories,
            'subcategories': subcategories,
            'countries': countries,
            'table_data': result
            }

    def get_indicators_statistics(self):
        """ Generate content for table in UNECE Environmental Indicators tab
        """
        countries = self.get_countries_folders()
        stats = {}
        for country in countries:
            stats[country.Title()] = get_indicators_statistics(country)
        return stats

    def get_national_reports_items(self):
        """ Return all published national reports found in this context
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        results = [x.getObject() for x in catalog.searchResults(
            {
                'portal_type': ['nationalreport'],
                'review_state': 'published',
                'path': '/'.join(self.context.getPhysicalPath())
            }
        )]

        return results

    def get_national_reports(self):
        """ Return national reports for countries
        """
        years = [
            (1990, u"1990"),
            (1991, u"'91"),
            (1992, u"'92"),
            (1993, u"'93"),
            (1994, u"'94"),
            (1995, u"'95"),
            (1996, u"'96"),
            (1997, u"'97"),
            (1998, u"'98"),
            (1999, u"'99"),
            (2000, u"2000"),
            (2001, u"'01"),
            (2002, u"'02"),
            (2003, u"'03"),
            (2004, u"'04"),
            (2005, u"'05"),
            (2006, u"'06"),
            (2007, u"'07"),
            (2008, u"'08"),
            (2009, u"'09"),
            (2010, u"2010"),
            (2011, u"'11"),
            (2012, u"'12"),
            (2013, u"'13"),
            (2014, u"'14"),
            (2015, u"'15"),
            (2016, u"'16"),
            (2017, u"'17"),
            (2018, u"'18"),
            (2019, u"'19"),
            (2020, u"2020")
        ]

        countries = [x.Title() for x in self.get_countries_folders()]

        countries_data = {}

        for country_name in countries:
            countries_data[country_name] = {}

        reports = self.get_national_reports_items()

        for report in reports:
            country_name = report.aq_parent.aq_parent.Title()
            for year in report.years:
                countries_data[country_name][year] = True

        return {
            "years": years,
            "countries": countries,
            "data": countries_data,
            "table_title": datetime.today().strftime('%B %Y')
        }

    def get_reports_statistics(self):
        """ Return reports statistics for given country
        """
        def report_class(report_status):
            """ Class used to give colors in reports table
            """
            report_status = report_status.lower()
            if 'annual' in report_status:
                return 'report-yes-annual'
            elif 'yes' in report_status:
                return 'report-yes'
            elif 'no' in report_status:
                return 'report-no'
            else:
                return 'report-no-data'

        reports_types = self.context.unrestrictedTraverse(
            'reports_data').get_reports_types().keys()

        stats = {}
        for country in self.get_countries_folders():
            stats[country.Title()] = {}
            reports = country.unrestrictedTraverse(
                'reports_data/get_reports')()
            for report in reports:
                stats[country.Title()][report.report_type] = {
                    'status': report.get_status(),
                    'report_class': report_class(report.get_status()),
                    'object': report
                }

            missing_reports = [
                x for x in reports_types if x not in [y.id for y in reports]
            ]
            for report in missing_reports:
                stats[country.Title()][report] = {
                    'status': 'N/A',
                    'report_class': 'report-no-data',
                    'object': None
                }
        return stats


class CountryViewEast(BrowserView):
    """ The view for a country (East)
    """
    def get_indicators_statistics(self):
        return get_indicators_statistics(self.context)

    def get_publications_pages(self):
        """ Return list of country publications pages
            from Publications folder
        """
        pages = self.context.portal_catalog.searchResults(
            portal_type=['Document', 'Folderish Document'],
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
            portal_type=['News Item', 'Folderish News Item'],
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

    def get_national_reports_description(self):
        """ Return title to be used in Report on the state environment tab
        """
        try:
            return self.context['national-reports'].Description()
        except Exception:
            return "Missing national-reports folder."

    def get_indicators_eea(self):
        """ Return the list of Indicators EEA for this country
        """
        this_country = self.context.Title()

        all_indicators = self.context.portal_catalog.searchResults(
            portal_type=['indicatordata'],
            review_state='published',
            sort_on='sortable_title',
            sort_order='ascending',
            path='/east/indicators'
        )
        country_indicators = []
        for ind in all_indicators:
            indicator = ind.getObject()
            countries = indicator.countries
            country_titles = [
                    EAST_COUNTRIES_DICT.get(x, '') for x in countries]
            if this_country in country_titles:
                country_indicators.append(indicator)

        return country_indicators


class ReportsDataView(BrowserView):
    """ Utils for Reports
    """
    utils = {
        'get_reports_types()':
            "Return possible types for a report",
        'get_reports()':
            "Return all published reports found in this context",
        'get_national_reports()':
            "Return all published national reports found in this context"
    }

    def get_reports_types(self):
        """ Return possible types for a report
        """
        terms = self.context.portal_vocabularies.getVocabularyByName(
            'environmental_assesment_reports_types').items()
        res = [(t[0], t[1].title) for t in terms]
        return OrderedDict(res)

    def get_reports(self):
        """ Return all published reports found in this context
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        results = [x.getObject() for x in catalog.searchResults(
            {
                'portal_type': ['report'],
                'review_state': 'published',
                'sort_on': 'getObjPositionInParent',
                'path': '/'.join(self.context.getPhysicalPath())
            }
        )]

        return results

    def get_national_reports(self):
        """ Return all published national reports found in this context
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        results = [x.getObject() for x in catalog.searchResults(
            {
                'portal_type': ['nationalreport'],
                'review_state': 'published',
                'sort_on': 'getObjPositionInParent',
                'path': '/'.join(self.context.getPhysicalPath())
            }
        )]

        return results

    def get_national_reports_country(self):
        """ Return all published national reports found in this context
            only reports having data
        """
        res = self.get_national_reports()
        results = [x for x in res if x.has_info() is True]

        return results

    def __call__(self):
        return self.utils


class ReportView(BrowserView):
    """ Report
    """


class NationalReportView(BrowserView):
    """ National Report
    """


class ProductItemView(BrowserView):
    """ Product Item
    """


class IndicatorsDataView(BrowserView):
    """ Utils for Indicators
    """
    utils = {
        'get_indicators_categories()':
            "Return possible categories for an indicator",
        'get_indicators_subcategories()':
            "Return possible subcategories for an indicator",
        'get_indicators()':
            "Return all published indicators found in this context"
    }

    def get_indicators_categories(self):
        """ Return possible categories for an indicator
        """
        return UNECE_INDICATORS_CATEGORIES

    def get_indicators_subcategories(self):
        """ Return possible subcategories for an indicator
        """
        return UNECE_INDICATORS_SUBCATEGORIES

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


class IndicatorDataView(BrowserView):
    """ Indicator Data
    """
    def grouped_coverage(self):
        """ Given an iterable of numbers, group them by range
        """
        def extract_years(data):
            """
                2003-2006 -> [2003, 2004, 2005, 2006]
                2000 -> [2000]
                abc -> invalid: abc
            """
            result = []
            invalid = False
            try:
                year = int(data)
                result.append(year)
                return result
            except ValueError:
                try:
                    years = data.split("-")
                    if len(years) == 2:
                        start = int(years[0])
                        end = int(years[1]) + 1
                        for year in range(start, end):
                            result.append(year)
                        return result
                    else:
                        invalid = True
                except Exception:
                    return "invalid: " + data

            if invalid is True:
                return "invalid: " + data

        years = [
            x for x in self.context.temporal_coverage.replace(
                ",", " ").replace(
                ";", " ").split(" ") if len(x) > 0]

        data = []
        for item in years:
            temp = extract_years(item)
            if "invalid" not in temp:
                for x in temp:
                    data.append(x)

        # [TODO] In this moment data contains the list of all years. Use this
        # as search filter later.

        source = [int(x) for x in sorted(set(data))]
        output = []

        def group_func(idx_nr):
            """ Used as comparator for grouping
            """
            index, number = idx_nr
            return index - number

        for _key, group in groupby(enumerate(source), group_func):
            result = [x[1] for x in group]

            if len(result) == 1:
                output.append("{0}".format(result[0]))
            else:
                output.append("{0}-{1}".format(result[0], result[-1]))

        return output

    def get_daviz_items(self):
        """ Return all data vizualizations found in this context
        """
        catalog = getToolByName(self.context, 'portal_catalog')
        results = [x.getObject() for x in catalog.searchResults(
            {
                'portal_type': ['DavizVisualization'],
                'review_state': 'published',
                'sort_on': 'getObjPositionInParent',
                'path': '/'.join(self.context.getPhysicalPath())
            }
        )]

        return results

    def figures(self):
        def get_ids(number):
            return ["chart-" + str(number), "table-" + str(number)]

        items = self.get_daviz_items()
        figures = []
        ids = 0

        dashboards_heights = self.context.dashboards_heights
        try:
            heights = [int(x) for x in dashboards_heights.split(",")]
        except Exception:
            heights = []

        dashboard_index = 0

        for item in items:
            try:
                annot = IAnnotations(item)
                dashboard = annot['eea.daviz.config.views'][2]['dashboards']
                if dashboard is not None:
                    try:
                        height = heights[dashboard_index]
                    except Exception:
                        height = 680
                    url = item.absolute_url()
                    figures.append(
                        {
                            'type': 'dashboard',
                            'url': url,
                            'chart_id': dashboard[0]['name'],
                            'valid': True,
                            'title': item.Description(),
                            'ids': get_ids(ids),
                            'height': height,
                            'text': item.body()
                        }
                    )
                    ids = ids + 2
                    dashboard_index += 1
                    continue

            except Exception:
                pass

            try:
                annot = IAnnotations(item)
                chart_id = annot[
                    'eea.daviz.config.views'][0]['chartsconfig']['charts'][
                            0]['id']
                url = item.absolute_url()
                figures.append(
                    {
                        'type': 'chart',
                        'url': url,
                        'chart_id': chart_id,
                        'valid': True,
                        'title': item.Description(),
                        'ids': get_ids(ids),
                        'text': item.body()
                    }
                )
            except Exception as err:
                figures.append(
                    {
                        'type': 'chart',
                        'url': url,
                        'chart_id': 'N/A',
                        'valid': False,
                        'title': 'Invalid',
                        'ids': get_ids(ids),
                        'text': ''
                    }
                )
                err = err
            ids = ids + 2
        return figures


class NewsletterView(BrowserView):
    """ Newsletter
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

        if len(indicators_container.getFolderContents()) > 0:
            return "Canceled. The indicators folder is not empty."

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


class UpgradeGenerateReportsViewEast(BrowserView):
    """ /upgrade_generate_reports_east to be unsed in a country section
        to create Reports folder with all types reports
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
            reports_container = country.unrestrictedTraverse(
                REPORTS_CONTAINER[0])
        except AttributeError:
            reports_container = api.content.create(
                container=country, type='Folder',
                title=REPORTS_CONTAINER[1])
            api.content.transition(obj=reports_container,
                                   transition='publish')

        if len(reports_container.getFolderContents()) > 0:
            return "Canceled. The reports folder is not empty."

        for report_type in REPORTS_TYPES_VOCAB:
            item = createContentInContainer(
                reports_container, "report",
                title=report_type.title, report_type=report_type.value,
                status='yes', status_details=''
            )
            api.content.transition(obj=item, transition='publish')

        return "Done. Please verify reports folder and its contents."


class GetUpcomingEventsView(BrowserView):
    """ Next future Event and eea.meetings items list
    """
    def __call__(self):
        now = DateTime()

        events = [
            b.getObject() for b in self.context.portal_catalog.searchResults(
                portal_type=['Event', 'Folderish Event', 'eea.meeting'],
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


def find_meeting_in_parents(context):
    """ If given context is added inside a meeting return meeting,
        else None.
    """
    if context.portal_type == "eea.meeting":
        return context
    else:
        parents = context.aq_inner.aq_parent.absolute_url().split('/')[3:]
        obj = api.portal.get()
        for item in parents:
            obj = obj.restrictedTraverse(item)
            if obj.portal_type == "eea.meeting":
                return obj
    return None


def user_is_participant(context, user=None):
    """ Check if user is registered to a meeting that has this context
        is its children (any level).
    """
    if user is None:
        user = api.user.get_current()
    meeting = find_meeting_in_parents(context)
    if meeting is None:
        return False
    else:
        subscribers = meeting.get_subscribers()
        if user.getProperty('email') in [x.email for x in subscribers]:
            return True
    return False


class UserRolesHere(BrowserView):
    """ Return a list of user roles in this context. Examples:
        Anonymous: ['anonymous']
        Site admintrator, Manager: ['admin']
        Authenticated: ['authenticated']
        registered for this meeting: ['authenticated', 'participant']
    """
    def __call__(self):
        roles = api.user.get_roles()
        result = []
        if 'Site Administrator' in roles or 'Manager' in roles:
            result.append('admin')

        if 'Authenticated' in roles:
            result.append('authenticated')

        if 'Anonymous' in roles:
            result.append('anonymous')

        if user_is_participant(context=self.context):
            result.append('participant')

        return result


class CanViewMeetingRestrictedContent(BrowserView):
    """ Return True if user is admin or participant of related meeting.
        To be used as added filter (in templates for example).
    """
    def __call__(self):
        meeting = find_meeting_in_parents(self.context)
        if meeting is not None:
            user_roles = self.context.restrictedTraverse('user_roles_here')()
            if 'admin' in user_roles or 'participant' in user_roles:
                return True
            else:
                return False
        return True


class NFPSList(BrowserView):
    """ Return National Focal Point items list in context
        - in country context return local nfps
        - in other context return the list of countries with their nfps
    """
    def get_countries_folders(self):
        """ Return list of countries folders
        """
        if 'south' in api.portal.get().absolute_url():
            COUNTRIES = SOUTH_COUNTRIES
            path = '/south/countries'
        else:
            COUNTRIES = EAST_COUNTRIES
            path = '/east/countries'

        folders = self.context.portal_catalog.searchResults(
            portal_type=['Folder'],
            review_state='published',
            sort_on='id',
            path=path
        )
        folders = [b.getObject() for b in folders]
        countries = [x for x in folders if x.Title() in COUNTRIES]
        return countries

    def get_country_nfps_list(self, context):
        """ Return nfps list for given context (country)
        """
        nfps = [
            b.getObject() for b in
            context.portal_catalog.searchResults(
                    portal_type=['nfp'],
                    review_state='published',
                    sort_on='getObjPositionInParent',
                    path='/'.join(context.getPhysicalPath())
                )
            ]
        return nfps

    def get_countries_nfps_list(self, context):
        """ Return nfps list for all countries
        """
        countries = self.get_countries_folders()
        nfps = []
        for country in countries:
            nfps.append({
                    country.title: self.get_country_nfps_list(country)
                })

        return nfps

    def __call__(self):
        portal = api.portal.get()
        is_country = True if self.context.aq_parent.absolute_url() == \
            portal.absolute_url() + '/countries' else False
        if is_country is True:
            return self.get_country_nfps_list(self.context)
        else:
            return self.get_countries_nfps_list(portal)
