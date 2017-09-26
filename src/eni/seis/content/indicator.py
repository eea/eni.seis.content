from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import IIndicator


@implementer(IIndicator)
class Indicator(Container):
    """ Indicator content type """

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
