""" Vocabularies for eni.seis.content
"""

from Products.ATVocabularyManager import NamedVocabulary
from plone import api
from zope.interface import alsoProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


EUROPEAN_COUNTRIES = {
    'ad':'ad',
    'al':'al',
    'am':'am',
    'at':'at',
    'az':'az',
    'ba':'ba',
    'be':'be',
    'bg':'bg',
    'by':'by',
    'ch':'ch',
    'cs':'cs',
    'cy':'cy',
    'cz':'cz',
    'de':'de',
    'dk':'dk',
    'ee':'ee',
    'es':'es',
    'fi':'fi',
    'fo':'fo',
    'fr':'fr',
    'gb':'gb',
    'ge':'ge',
    'gr':'gr',
    'hr':'hr',
    'hu':'hu',
    'ie':'ie',
    'il':'il',
    'is':'is',
    'it':'it',
    'kz':'kz',
    'li':'li',
    'lt':'lt',
    'lu':'lu',
    'lv':'lv',
    'mc':'mc',
    'md':'md',
    'mk':'mk',
    'mt':'mt',
    'nl':'nl',
    'no':'no',
    'pl':'pl',
    'pt':'pt',
    'ro':'ro',
    'ru':'ru',
    'se':'se',
    'si':'si',
    'sk':'sk',
    'sm':'sm',
    'tr':'tr',
    'ua':'ua',
}


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
