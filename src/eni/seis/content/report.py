from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import IReport


REPORT_META_TYPE = 'Report'


@implementer(IReport)
class Report(Container):
    """ Report content type """

    meta_type = REPORT_META_TYPE

    def has_data(self):
        """ [TODO] Return True if it has a link or a file, else False
        """
        return False

    def has_external_link(self):
        """ [TODO] Return True if it has a link or a file, else False
        """
        return False

    def has_file(self):
        """ [TODO] Return True if it has a link or a file, else False
        """
        return False
