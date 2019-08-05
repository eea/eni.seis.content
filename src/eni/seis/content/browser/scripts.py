from eni.seis.content.browser.misc import compute_broken_links

HOST = 'eni-seis.eionet.europa.eu'


def get_plone_site(PLONE):
    import Zope2
    app = Zope2.app()
    from Testing.ZopeTestCase import utils
    utils._Z2HOST = HOST

    path = PLONE.split('/')

    app = utils.makerequest(app)
    app.REQUEST['PARENTS'] = [app]
    app.REQUEST.other['VirtualRootPhysicalPath'] = path
    from zope.globalrequest import setRequest
    setRequest(app.REQUEST)

    from AccessControl.SpecialUsers import system as user
    from AccessControl.SecurityManagement import newSecurityManager
    newSecurityManager(None, user)

    _site = app[path[-1]]
    site = _site.__of__(app)

    from zope.site.hooks import setSite
    setSite(site)

    return site


def get_broken_links():
    """ A cron callable script to get data regarding broken links
    This should be run through the zope client script running machinery,:
    bin/www1 run bin/get_broken_links
    """
    PLONES = ["/east", "/south"]
    for PLONE in PLONES:
        site = get_plone_site("/east")
        compute_broken_links(site)
