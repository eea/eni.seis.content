"""Common configuration constants
"""
from collections import OrderedDict
from zope.i18nmessageid import MessageFactory as MF
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

MessageFactory = MF('eni.seis')

ALL_REPORTS_CATEGORIES = OrderedDict([
    ("A", "Air pollution and ozone depletion"),
    ("B", "Climate change"),
    ("C", "Water"),
    ("D", "Biodiversity"),
    ("E", "Land and soil"),
    ("F", "Agriculture"),
    ("G", "Energy"),
    ("H", "Transport"),
    ("I", "Waste"),
    ("J", "Environmental financing")
])

UNECE_INDICATORS_CATEGORIES = OrderedDict([
    ("A", "Air pollution and ozone depletion"),
    ("B", "Climate change"),
    ("C", "Water"),
    ("D", "Biodiversity"),
    ("E", "Land and soil"),
    ("F", "Agriculture"),
    ("G", "Energy"),
    ("H", "Transport"),
    ("I", "Waste"),
    ("J", "Environmental financing")
])

EAST_COUNTRIES = [
    'Armenia',
    'Azerbaijan',
    'Belarus',
    'Georgia',
    'Moldova',
    'Ukraine'
]

REPORT_CATEGORIES_VOCAB = SimpleVocabulary(
    [
        SimpleTerm(
            value=x,
            title=x + ". " + ALL_REPORTS_CATEGORIES[x])
        for x in ALL_REPORTS_CATEGORIES.keys()
    ]
)
