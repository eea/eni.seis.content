import logging
from plone import api


logger = logging.getLogger('eni.seis.content')


def run(_):
    """ Delete Subnational environmental reports
    """
    catalog = api.portal.get_tool(name='portal_catalog')
    reports = [b.getObject() for b in catalog(portal_type='report')]
    deprecated_reports = [
        x for x in reports if x.id == 'subnational-environmental-reports']

    api.content.delete(objects=deprecated_reports)
