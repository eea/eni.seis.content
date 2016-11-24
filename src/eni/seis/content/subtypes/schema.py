""" Schema extender
"""
from zope.interface import implementer
from Products.Archetypes import public
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.field import ExtensionField
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from eni.seis.content.interfaces import IEniSeisContentLayer
from eni.seis.content.config import MessageFactory as _


class CountriesField(ExtensionField, public.LinesField):
    """ Schema extender
    """


class ExtendedStringField(ExtensionField, public.StringField):
    """ Extended StringField
    """


@implementer(ISchemaExtender, IBrowserLayerAwareExtender)
class EventSchemaExtender(object):
    """ Schema extender
    """
    layer = IEniSeisContentLayer

    fields = (
        CountriesField(
            name='countries',
            schemata='default',
            multiValued=1,
            vocabulary=NamedVocabulary('european_countries'),
            widget=public.MultiSelectionWidget(
                label=_(u"Countries"),
                description=_(u"Countries")
            )
        ),

        ExtendedStringField(
            name='event_level',
            widget=public.SelectionWidget(
                label="Event Level",
                description=(u"Select Regional Level for events that belong "
                             u"to both East and South")
            ),
            default="National Level",
            required=True,
            vocabulary=["National Level", "Regional Level"],
        ),
    )

    def __init__(self, context):
        self.context = context

    def getFields(self):
        """ Returns fields
        """
        return self.fields
