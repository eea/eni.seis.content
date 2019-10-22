from plone.indexer.decorator import indexer
from eni.seis.content.interfaces import IIndicatorData
from eni.seis.content.config import EAST_COUNTRIES_DICT


@indexer(IIndicatorData)
def indicatordata_topics(context):
    return context.topics


@indexer(IIndicatorData)
def indicatordata_indicator_code(context):
    return context.indicator_code


@indexer(IIndicatorData)
def indicatordata_temporal_coverage(context):
    return context.temporal_coverage


@indexer(IIndicatorData)
def indicatordata_dpsir(context):
    return context.dpsir


@indexer(IIndicatorData)
def indicatordata_typology(context):
    return context.typology


@indexer(IIndicatorData)
def indicatordata_countries(context):
    return [EAST_COUNTRIES_DICT.get(x, None) for x in context.countries]
