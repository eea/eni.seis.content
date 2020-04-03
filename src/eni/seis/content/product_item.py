from zope.interface import implementer
from plone.dexterity.content import Container
from eni.seis.content.interfaces import IProductItem


@implementer(IProductItem)
class ProductItem(Container):
    """ ProductItem content type """

    def get_view_url(self):
        """ Return its external link or file download url if exists
            OR absolute_url
            (because in some cases a report can act like a page with links or
            some other content)
        """
        if self.has_file():
            return self.absolute_url() + "/@@download/file"

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

    def files_listing(self):
        """ Return the files and links to be listed in table
        """
        contents = [x.getObject() for x in self.getFolderContents()]
        listing = []
        for item in contents:
            listing.append(
                (
                    item.Title(),
                    item.absolute_url(),
                    item.portal_type
                )
            )
        return listing

    def has_multiple_files(self):
        """ Return True if it has multiple File or Link items added in its
            container
        """
        return True if len(self.getFolderContents()) > 0 else False
