from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import INationalFocalPoint


NFP_META_TYPE = 'nfp'


@implementer(INationalFocalPoint)
class NationalFocalPoint(Container):
    """ nfp content type """

    meta_type = NFP_META_TYPE
