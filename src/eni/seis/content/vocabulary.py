""" Vocabularies for eni.seis.content
"""

from collections import OrderedDict
from plone import api
from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


EUROPEAN_COUNTRIES = {
    'ad': 'ad',
    'al': 'al',
    'am': 'am',
    'at': 'at',
    'az': 'az',
    'ba': 'ba',
    'be': 'be',
    'bg': 'bg',
    'by': 'by',
    'ch': 'ch',
    'cs': 'cs',
    'cy': 'cy',
    'cz': 'cz',
    'de': 'de',
    'dk': 'dk',
    'ee': 'ee',
    'es': 'es',
    'fi': 'fi',
    'fo': 'fo',
    'fr': 'fr',
    'gb': 'gb',
    'ge': 'ge',
    'gr': 'gr',
    'hr': 'hr',
    'hu': 'hu',
    'ie': 'ie',
    'il': 'il',
    'is': 'is',
    'it': 'it',
    'kz': 'kz',
    'li': 'li',
    'lt': 'lt',
    'lu': 'lu',
    'lv': 'lv',
    'mc': 'mc',
    'md': 'md',
    'mk': 'mk',
    'mt': 'mt',
    'nl': 'nl',
    'no': 'no',
    'pl': 'pl',
    'pt': 'pt',
    'ro': 'ro',
    'ru': 'ru',
    'se': 'se',
    'si': 'si',
    'sk': 'sk',
    'sm': 'sm',
    'tr': 'tr',
    'ua': 'ua',
}

SUBSCRIBER_ROLES = {
    'eni-seis-ii-south-nfp': 'ENI-SEIS II South NFP',
    'medpol-nfp': 'MedPOL NFP',
    'h2020-nfp': 'H2020 NFP',
    'other': 'Other',
}

EAST_LANGUAGES = {
    "EN": "EN",
    "AM": "AM",
    "AZ": "AZ",
    "BY": "BY",
    "GE": "GE",
    "MD": "MD",
    "UA": "UA"
}

EAST_PRODUCTS_CATEGORIES = {
    u"Maturity Report": u"AEI - 1: Maturity Report",
    u"Roadmap": u"AEI - 2: Roadmap",
    u"Executive Summary": u"AEI - 3: Executive Summary",
    u"Good practice": u"AEI - 4: Good practice",

    u"Technical Reports": u"Land - 1: Technical Reports",
    u"Corine Land Cover Change Analysis":
    u"Land - 2: Corine Land Cover Change Analysis",
    u"Link to Copernicus": u"Land - 3: Link to Copernicus",
    u"Summary of Final Technical Report":
    u"Land - 4: Summary of Final Technical Report"
}


def _create_east_languages_vocabulary():
    """ To be used for national reports
    """
    for x, y in EAST_LANGUAGES.items():
        term = SimpleTerm(value=x, token=x, title=y)
        yield term


def _create_east_products_categories_vocabulary():
    """ To be used for national reports
    """
    categories = OrderedDict(
        sorted(EAST_PRODUCTS_CATEGORIES.items(), key=lambda t: t[1]))

    for x, y in categories.items():
        term = SimpleTerm(value=x, token=x, title=y)
        yield term


EAST_LANGUAGES_VOCABULARY = SimpleVocabulary(
    list(_create_east_languages_vocabulary())
)

EAST_PRODUCTS_CATEGORIES_VOCABULARY = SimpleVocabulary(
    list(_create_east_products_categories_vocabulary())
)


def _create_east_years_vocabulary():
    """ To be used for national reports
    """
    for x in range(1990, 2021):
        term = SimpleTerm(value=x, token=x, title=x)
        yield term


EAST_YEARS_VOCABULARY = SimpleVocabulary(
    list(_create_east_years_vocabulary())
)


def atvocabulary_to_zope_vocab(name):
    """ Constructs a vocabulary factory for interop with ATVocabularyManager
    """

    def factory(context):
        atvm = api.portal.get_tool(name='portal_vocabularies')
        nv = atvm.getVocabularyByName(name)
        _terms = dict(nv.getVocabularyDict(nv))

        return SimpleVocabulary([
            SimpleTerm(n, n.encode('utf-8'), l) for n, l in _terms.items()
        ])

    return factory


countries_vocabulary = atvocabulary_to_zope_vocab('european_countries')
alsoProvides(countries_vocabulary, IVocabularyFactory)

subscriber_roles_vocabulary = atvocabulary_to_zope_vocab('subscriber_roles')
alsoProvides(subscriber_roles_vocabulary, IVocabularyFactory)

environmental_assesment_reports_types_vocabulary = atvocabulary_to_zope_vocab(
    'environmental_assesment_reports_types')
alsoProvides(
    environmental_assesment_reports_types_vocabulary, IVocabularyFactory)
