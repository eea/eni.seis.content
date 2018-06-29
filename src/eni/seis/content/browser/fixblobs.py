"""
    A Zope command line script to delete content with missing BLOB in Plone,
    causing POSKeyErrors when content is being accessed or during
    portal_catalog rebuild.

    Tested on Plone 4.1 + Dexterity 1.1.

    http://stackoverflow.com/questions/8655675/
    cleaning-up-poskeyerror-no-blob-file-content-from-plone-site

    Also see:

    https://pypi.python.org/pypi/experimental.gracefulblobmissing/

"""

# Zope imports
from ZODB.POSException import POSKeyError
from zope.component import queryUtility
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFCore.interfaces import IFolderish

# Plone imports
from Products.Five import BrowserView
from Products.Archetypes.Field import FileField
from Products.Archetypes.interfaces import IBaseContent
from plone.namedfile.interfaces import INamedFile
from plone.dexterity.content import DexterityContent


def check_at_blobs(context):
    """ Archetypes content checker.

    Return True if purge needed
    """

    if IBaseContent.providedBy(context):

        schema = context.Schema()
        for field in schema.fields():
            id = field.getName()
            if isinstance(field, FileField):
                try:
                    field.get_size(context)
                except POSKeyError:
                    print "Found damaged AT FileField %s on %s" % (
                            id, context.absolute_url())
                    return True

    return False


def check_dexterity_blobs(context):
    """ Check Dexterity content for damaged blob fields

    XXX: NOT TESTED - THEORETICAL, GUIDELINING, IMPLEMENTATION

    Return True if purge needed
    """

    # Assume dexterity contennt inherits from Item
    if isinstance(context, DexterityContent):

        # Iterate through all Python object attributes
        # XXX: Might be smarter to use zope.schema introspection here?
        for key, value in context.__dict__.items():
            # Ignore non-contentish attributes to speed up us a bit
            if not key.startswith("_"):
                if INamedFile.providedBy(value):
                    try:
                        value.getSize()
                    except POSKeyError:
                        print "Found damaged Dexterity plone.app.NamedFile \
                                %s on %s" % (key, context.absolute_url())
                        return True
    return False


def fix_blobs(context, only_check=True):
    """
    Iterate through the object variables and see if they are blob fields
    and if the field loading fails then poof

    only_check = False if you really want to delete the objects
    """

    if check_at_blobs(context) or check_dexterity_blobs(context):
        print "Bad blobs found on %s" % context.absolute_url() + " -> deleting"
        parent = context.aq_parent
        if only_check is False:
            parent.manage_delObjects([context.getId()])


def fix_blobs_advanced(context, only_check=True):
    """ Discover other bad objects which are not found by fix_blobs,
        but returns the same No blob file error
    """
    try:
        context.get_size()
    except Exception as e:
        e = e
        # import pdb; pdb.set_trace()
        print "MAYBE: {0}".format(context.absolute_url())


def recurse(tree, only_check=True):
    """ Walk through all the content on a Plone site

        only_check = False if you really want to delete the objects
    """
    for id, child in tree.contentItems():

        fix_blobs(child, only_check=only_check)
        fix_blobs_advanced(child, only_check=only_check)

        if IFolderish.providedBy(child):
            recurse(child, only_check=only_check)


class FixBlobsOnlyCheck(BrowserView):
    """
        The same as FixBlobs but do not delete objects only list them
    """
    def disable_integrity_check(self):
        """ Content HTML may have references to this broken image - we cannot
        fix that HTML but link integrity check will yell if we try to
        delete the bad image.
        """

        ptool = queryUtility(IPropertiesTool)
        props = getattr(ptool, 'site_properties', None)
        self.old_check = props.getProperty(
                'enable_link_integrity_checks', False)
        props.enable_link_integrity_checks = False

    def enable_integrity_check(self):
        """ """
        ptool = queryUtility(IPropertiesTool)
        props = getattr(ptool, 'site_properties', None)
        props.enable_link_integrity_checks = self.old_check

    def render(self):
        # plone = getMultiAdapter(
        # (self.context, self.request), name="plone_portal_state")
        print "Checking blobs"
        portal = self.context
        self.disable_integrity_check()
        recurse(portal, only_check=True)
        self.enable_integrity_check()
        print "All done"
        return "OK - check console for status messages"

    def __call__(self):
        self.render()


class FixBlobs(BrowserView):
    """
    A management view to clean up content with damaged BLOB files

    You can call this view by

    1) Starting Plone in debug mode (console output available)

    2) Visit site.com/@@fix-blobs URL

    """
    def disable_integrity_check(self):
        """ Content HTML may have references to this broken image - we cannot
        fix that HTML but link integrity check will yell if we try to
        delete the bad image.
        """

        ptool = queryUtility(IPropertiesTool)
        props = getattr(ptool, 'site_properties', None)
        self.old_check = props.getProperty(
                'enable_link_integrity_checks', False)
        props.enable_link_integrity_checks = False

    def enable_integrity_check(self):
        """ """
        ptool = queryUtility(IPropertiesTool)
        props = getattr(ptool, 'site_properties', None)
        props.enable_link_integrity_checks = self.old_check

    def render(self):
        # plone = getMultiAdapter(
        # (self.context, self.request), name="plone_portal_state")
        print "Checking blobs"
        portal = self.context
        self.disable_integrity_check()
        recurse(portal, only_check=False)
        self.enable_integrity_check()
        print "All done"
        return "OK - check console for status messages"

    def __call__(self):
        self.render()
