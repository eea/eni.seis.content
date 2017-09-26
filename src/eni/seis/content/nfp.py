from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import INationalFocalPoint


@implementer(INationalFocalPoint)
class NationalFocalPoint(Container):
    """ nfp content type """
