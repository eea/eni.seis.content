from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import IReport
from eni.seis.content.config import REPORTS_STATUS_TYPES


REPORT_META_TYPE = 'Report'


@implementer(IReport)
class Report(Container):
    """ Report content type """

    meta_type = REPORT_META_TYPE

    def has_external_link(self):
        """ Return True if it has a link, else False
        """
        if self.external_link:
            return True
        return False

    def has_file(self):
        """ Return True if it has a file, else False
        """
        if self.file:
            return True
        return False

    def has_data(self):
        """ Return True if it has a link or a file, else False
        """
        return self.has_external_link() or self.has_file()

    def get_status(self):
        """ Return the status of the report
            Example: Yes / Annual
        """
        status = ""
        if self.status is not None:
            status = REPORTS_STATUS_TYPES[self.status]
            if len(self.status_details) > 0:
                status = status + " / " + self.status_details
        return status
