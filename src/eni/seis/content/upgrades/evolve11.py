import logging
from plone import api
from eni.seis.content.config import REPORTS_CONTAINER
from eni.seis.content.config import EAST_COUNTRIES

logger = logging.getLogger('eni.seis.content')


report_links = {
    "Azerbaijan": u"https://sustainabledevelopment.un.org/content/" +
    "documents/14974Azerbaijan.pdf",
    "Armenia": u"https://sustainabledevelopment.un.org/content/" +
    "documents/800Armenia_Report_Final.pdf",
    "Belarus": u"https://sustainabledevelopment.un.org/content/" +
    "documents/792belarus.pdf",
    "Georgia": u"https://sustainabledevelopment.un.org/content/" +
    "documents/1511Georgia%20national%20reviews.pdf",
    "Moldova": u"http://md.one.un.org/content/dam/unct/moldova/" +
    "docs/pub/mdg/3rdMDGReport_Eng.pdf",
    "Ukraine": u"http://www.un.org.ua/images/SDGs_NationalReportEN_Web.pdf"
}


def run(_):
    """ Upgrade reports used in countries section
    """
    # Delete Subnational environmental reports
    catalog = api.portal.get_tool(name='portal_catalog')
    reports = [b.getObject() for b in catalog(portal_type='report')]
    old_reports_types = [
        'local-environmental-reports',
        'subnational-environmental-reports']

    deprecated_reports = [
        x for x in reports if x.id in old_reports_types]

    api.content.delete(objects=deprecated_reports)

    # Add Report on sustainable development for East countries
    new_report_title = u"Report on sustainable development"
    new_report_type = u"report-on-sustainable-development"

    site = api.portal.get()
    try:
        site.unrestrictedTraverse('countries/armenia')
        is_east = True
    except Exception:
        is_east = False

    if is_east:
        countries_folder = site.unrestrictedTraverse('countries')
        for country_title in EAST_COUNTRIES:
            country = countries_folder.unrestrictedTraverse(
                country_title.lower())
            reports_container = country.unrestrictedTraverse(
                REPORTS_CONTAINER[0])
            new_report = api.content.create(
                container=reports_container, type="report",
                title=new_report_title,
                report_type=new_report_type,
                external_link=report_links.get(country_title, ""),
                status='yes', status_details='')
            api.content.transition(obj=new_report, transition='publish')
