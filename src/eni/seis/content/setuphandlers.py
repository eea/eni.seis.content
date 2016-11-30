""" Generic Setup
"""
import logging
from zope.interface import implementer
from zope.component import queryUtility
from zope.component.hooks import getSite
from plone.i18n.locales.interfaces import ICountryAvailability
from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFCore.utils import getToolByName
from eni.seis.content.vocabulary import EUROPEAN_COUNTRIES

logger = logging.getLogger('eni.seis')

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'eni.seis.content:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def getCountries():
    """ Setup Countries Vocabulary
    """
    res = {}
    util = queryUtility(ICountryAvailability)
    all_countries = util.getCountries()
    for code in EUROPEAN_COUNTRIES:
        country_name = all_countries[code][u'name']
        res[code] = country_name
    return res

def setup_media_events(site):
    """ Update Site > Media > Events view
    """
    if 'media' not in site.objectIds():
        return

    media = site['media']
    if 'events' not in media.objectIds():
        return

    events = media['events']
    events.setLayout('eni_events_listing')

def setup_portal_vocabularies(site):
    """ Portal vocabularies
    """
    atvm = getToolByName(site, 'portal_vocabularies')
    if not atvm:
        logger.warn('No portal_vocabularies. Nothing to do.')
        return

    if 'european_countries' in atvm.objectIds():
        logger.warn('european_countries already imported. Nothing to do.')
        return

    countries = getCountries()
    atvm.invokeFactory('SimpleVocabulary', 'european_countries')
    voc = atvm.getVocabularyByName('european_countries')
    for key, val in countries.items():
        logger.info('Adding country %s: %s within europea_countries vocabulary', key, val)
        voc.addTerm(key, val)


def setup_various(context):
    """Post install script"""
    # Do something at the end of the installation of this package.

    if context.readDataFile('eni.seis.txt') is None:
        return

    site = getSite()
    setup_media_events(site)
    setup_portal_vocabularies(site)
