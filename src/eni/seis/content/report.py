from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import IReport
from eni.seis.content.config import REPORTS_STATUS_TYPES


@implementer(IReport)
class Report(Container):
    """ Report content type """

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

    def get_view_url(self):
        """ Return its external link if exists or absolute_url
            (because in some cases a report can act like a page with links or
            some other content)
        """
        if self.has_external_link():
            return self.external_link
        return self.absolute_url()

    def get_status(self):
        """ Return the status of the report
            Example: Yes / Annual
        """
        status = ""
        if self.status is not None:
            status = REPORTS_STATUS_TYPES[self.status]
            if self.status_details and len(self.status_details) > 0:
                status = status + " / " + self.status_details
        return status
