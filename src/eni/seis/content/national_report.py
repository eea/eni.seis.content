from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import INationalReport


@implementer(INationalReport)
class NationalReport(Container):
    """ National Report content type """

    def get_view_url(self):
        """ Return its external link if exists or absolute_url
            (because in some cases a report can act like a page with links or
            some other content)
        """
        if self.has_external_link():
            return self.external_link
        return self.absolute_url()

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
