"""Common configuration constants
"""
from collections import OrderedDict
from zope.i18nmessageid import MessageFactory as MF
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

MessageFactory = MF('eni.seis')

ALL_REPORTS_CATEGORIES = OrderedDict([
    (u"national-environmental-reports", u"National environmental reports"),
    (u"subnational-environmental-reports",
        u"Subnational environmental reports"),
    (u"local-environmental-reports",
     u"Local environmental reports"),
    (u"specialized-reports-climate-national-communications-to-unfccc",
     u"Specialized reports - climate (national communications to UNFCCC)"),
    (u"specialized-reports-air",
     u"Specialized reports - air"),
    (u"specialied-reports-water",
     u"Specialized reports - water"),
    (u"specialized-reports-biodiversity",
        u"Specialized reports - biodiversity"),
    (u"specialized-reports-waste", u"Specialized reports - waste"),
    (u"indicator-based-reports", u"Indicator-based reports"),
    (u"national-statistical-yearbook", u"National Statistical Yearbook"),
    (u"national-statistical-yearbook-on-environment",
        u"National Statistical Yearbook on environment")
])

UNECE_INDICATORS_CONTAINER = (
        'unece-environmental-indicators', "UNECE Environmental Indicators"
    )

UNECE_INDICATORS_CATEGORIES = OrderedDict([
    (u"A", u"Air pollution and ozone depletion"),
    (u"B", u"Climate change"),
    (u"C", u"Water"),
    (u"D", u"Biodiversity"),
    (u"E", u"Land and soil"),
    (u"F", u"Agriculture"),
    (u"G", u"Energy"),
    (u"H", u"Transport"),
    (u"I", u"Waste"),
    (u"J", u"Environmental financing")
])

UNECE_INDICATORS_SUBCATEGORIES = OrderedDict([
    (u"A1", u"Emissions of pollutants into the atmospheric air"),
    (u"A2", u"Ambient air quality in urban areas"),
    (u"A3", u"Consumption of ozone-depleting substances"),

    (u"B1", u"Air temperature"),
    (u"B2", u"Atmospheric precipitation"),
    (u"B3", u"Greenhouse gas emissions"),

    (u"C1", u"Renewable freshwater resources"),
    (u"C2", u"Freshwater abstraction"),
    (u"C3", u"Total water use"),
    (u"C4", u"Household water use per capita"),
    (u"C5", u"Water supply industry and population connected to water "
        "supply industry"),
    (u"C6", u"Connection of population to public water supply"),
    (u"C7", u"Water losses"),
    (u"C8", u"Reuse and recycling of freshwater"),
    (u"C9", u"Drinking water quality"),
    (u"C10", u"BOD and concentration of ammonium in rivers"),
    (u"C11", u"Nutrients in freshwater"),
    (u"C12", u"Nutrients in coastal seawaters"),
    (u"C13", u"Concentrations of pollutants in coastal seawater and "
        "sediments (except nutrients)"),
    (u"C14", u"Population connected to wastewater treatment"),
    (u"C15", u"Wastewater treatment facilities"),
    (u"C16", u"Polluted (non-treated) wastewaters"),

    (u"D1", u"Protected areas"),
    (u"D2", u"Biosphere reserves and wetlands of international "
        "importance"),
    (u"D3", u"Forests and other wooded land"),
    (u"D4", u"Threatened and protected species"),
    (u"D5", u"Trends in the number and distribution of selected species"),
    (u"D6", u"Invasive alien species"),

    (u"E1", u"Land uptake"),
    (u"E2", u"Area affected by soil erosion"),

    (u"F1", u"Irrigation"),
    (u"F2", u"Fertilizer consumption"),
    (u"F3", u"Gross nitrogen balance"),
    (u"F4", u"Pesticide consumption"),

    (u"G1", u"Final energy consumption"),
    (u"G2", u"Total primary energy supply"),
    (u"G3", u"Energy intensity"),
    (u"G4", u"Renewable energy consumption"),
    (u"G5", u"Final electricity consumption"),
    (u"G6", u"Gross electricity production"),

    (u"H1", u"Passenger transport demand"),
    (u"H2", u"Freight transport demand"),
    (u"H3", u"Composition of road motor vehicle fleet by fuel type"),
    (u"H4", u"Age of road motor vehicle fleet"),

    (u"I1", u"Waste generation"),
    (u"I2", u"Management of hazardous waste"),
    (u"I3", u"Waste reuse and recycling"),
    (u"I4", u"Final waste disposal"),

    (u"J1", u"Environment protection expenditure")
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

UNECE_INDICATORS_CATEGORIES_VOCAB = SimpleVocabulary(
    [
        SimpleTerm(
            value=x,
            title=x + ". " + UNECE_INDICATORS_CATEGORIES[x])
        for x in UNECE_INDICATORS_CATEGORIES.keys()
    ]
)

UNECE_INDICATORS_SUBCATEGORIES_VOCAB = SimpleVocabulary(
    [
        SimpleTerm(
            value=x,
            title=x + ". " + UNECE_INDICATORS_SUBCATEGORIES[x])
        for x in UNECE_INDICATORS_SUBCATEGORIES.keys()
    ]
)
