from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import INewsletter


@implementer(INewsletter)
class Newsletter(Container):
    """ Newsletter content type """

    def has_link(self):
        """ Return True if it has a link, else False
        """
        if self.link:
            return True
        return False

    def has_file(self):
        """ Return True if it has a file, else False
        """
        if self.file:
            return True
        return False

    def get_view_url(self):
        """ Return its link if exists or absolute_url
        """
        if self.has_link():
            return self.link
        return self.absolute_url()
