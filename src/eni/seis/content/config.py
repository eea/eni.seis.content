"""Common configuration constants
"""
from collections import OrderedDict
from zope.i18nmessageid import MessageFactory as MF
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

MessageFactory = MF('eni.seis')

ALL_REPORTS_CATEGORIES = OrderedDict([
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
    (u"A1", u"A1. Emissions of pollutants into the atmospheric air"),
    (u"A2", u"A2. Ambient air quality in urban areas"),
    (u"A3", u"A3. Consumption of ozone-depleting substances"),

    (u"B1", u"B1. Air temperature"),
    (u"B2", u"B2. Atmospheric precipitation"),
    (u"B3", u"B3. Greenhouse gas emissions"),

    (u"C1", u"C1. Renewable freshwater resources"),
    (u"C2", u"C2. Freshwater abstraction"),
    (u"C3", u"C3. Total water use"),
    (u"C4", u"C4. Household water use per capita"),
    (u"C5", u"C5. Water supply industry and population connected to water "
        "supply industry"),
    (u"C6", u"C6. Connection of population to public water supply"),
    (u"C7", u"C7. Water losses"),
    (u"C8", u"C8. Reuse and recycling of freshwater"),
    (u"C9", u"C9. Drinking water quality"),
    (u"C10", u"C10. BOD and concentration of ammonium in rivers"),
    (u"C11", u"C11. Nutrients in freshwater"),
    (u"C12", u"C12. Nutrients in coastal seawaters"),
    (u"C13", u"C13. Concentrations of pollutants in coastal seawater and "
        "sediments (except nutrients)"),
    (u"C14", u"C14. Population connected to wastewater treatment"),
    (u"C15", u"C15. Wastewater treatment facilities"),
    (u"C16", "C16. Polluted (non-treated) wastewaters"),

    (u"D1", u"D1. Protected areas"),
    (u"D2", u"D2. Biosphere reserves and wetlands of international "
        "importance"),
    (u"D3", u"D3. Forests and other wooded land"),
    (u"D4", u"D4. Threatened and protected species"),
    (u"D5", u"D5. Trends in the number and distribution of selected species"),
    (u"D6", u"D6. Invasive alien species"),

    (u"E1", u"E1. Land uptake"),
    (u"E2", u"E2. Area affected by soil erosion"),

    (u"F1", u"F1. Irrigation"),
    (u"F2", u"F2. Fertilizer consumption"),
    (u"F3", u"F3. Gross nitrogen balance"),
    (u"F4", u"F4. Pesticide consumption"),

    (u"G1", u"G1. Final energy consumption"),
    (u"G2", u"G2. Total primary energy supply"),
    (u"G3", u"G3. Energy intensity"),
    (u"G4", u"G4. Renewable energy consumption"),
    (u"G5", u"G5. Final electricity consumption"),
    (u"G6", u"G6. Gross electricity production"),

    (u"H1", u"H1. Passenger transport demand"),
    (u"H2", u"H2. Freight transport demand"),
    (u"H3", u"H3. Composition of road motor vehicle fleet by fuel type"),
    (u"H4", u"H4. Age of road motor vehicle fleet"),

    (u"I1", u"I1. Waste generation"),
    (u"I2", u"I2. Management of hazardous waste"),
    (u"I3", u"I3. Waste reuse and recycling"),
    (u"I4", u"I4. Final waste disposal"),

    (u"J1", u"J1. Environment protection expenditure")
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
