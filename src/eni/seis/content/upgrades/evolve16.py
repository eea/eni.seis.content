from plone import api
import logging

logger = logging.getLogger('eni.seis.content')


def run(_):
    reindex_indicatordata_items(logger)


def reindex_indicatordata_items(logger):
    catalog = api.portal.get_tool('portal_catalog')

    brains = catalog(portal_type='indicatordata')
    brains_len = len(brains)
    logger.info('Found %s brains.', brains_len)
    indicatordata_items = (brain.getObject() for brain in brains)
    for idx, indicatordata in enumerate(indicatordata_items, start=1):
        catalog.catalog_object(indicatordata, idxs=tuple(), update_metadata=1)
        if idx % 50 == 0:
            logger.info('Done %s/%s.', idx, brains_len)
