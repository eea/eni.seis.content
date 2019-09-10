from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import IIndicatorData


@implementer(IIndicatorData)
class IndicatorData(Container):
    """ IndicatorData content type """
