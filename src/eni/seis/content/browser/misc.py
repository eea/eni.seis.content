from BeautifulSoup import BeautifulSoup
from Products.CMFPlone.utils import getToolByName
from zope.annotation.interfaces import IAnnotations
import logging
import re
import requests
import transaction


logger = logging.getLogger('eni.seis.content')


def convert_to_string(item):
    """ Convert to string other types
    """
    if not item:
        return ''
    if not isinstance(item, basestring):
        new_item = ""
        try:
            iterator = iter(item)
        except TypeError, err:
            value = getattr(item, 'raw', None)
            if value:
                return value
            logger.error(err)
            return ''
        else:
            for i in iterator:
                new_item += i
        return new_item
    return item


def discover_links(string_to_search):
    """ Use regular expressions to get all urls in string
    """
    # REGEX = re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.]
    # [a-z]{2,4}/)(?:[^\s()<>]|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>
    # ]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'\".,<>?\xab\xbb\u201c\u201d\u2018
    # \u2019]))')
    REGEX = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    try:
        result = re.findall(REGEX, string_to_search) or []
        if isinstance(result, basestring):
            result = [result]
    except Exception, err:
        logger.error(err)
        result = []
    return result


def compute_broken_links(site):
    """ Script that will get called by cron once per day
    """
    links = get_links(site)

    results = []

    for info in links:
        res = check_link(info['link'])

        if res is not None:
            res['object_url'] = info['object_url']
            results.append(res)

    IAnnotations(site)['broken_links_data'] = results
    transaction.commit()


def get_links(site):
    """ Gets the links for all our items by using the websites field
        along with the respective object urls
    """

    catalog = getToolByName(site, 'portal_catalog')
    query = {
        'portal_type': [
            # TODO add portal types
        ]
    }
    brains = catalog.searchResults(**query)
    urls = []

    append_urls = lambda link, path: urls.append({
        'link': link,
        'object_url': path
    })
    count = 0
    logger.info('Got %s objects' % len(brains))
    for b in brains:
        obj = b.getObject()
        path = obj.getPhysicalPath()
        if hasattr(obj, 'websites'):
            if isinstance(obj.websites, str):
                append_urls(obj.websites, path)
            else:
                for url in obj.websites:
                    append_urls(url, path)
        else:
            if obj.portal_type == 'eea.climateadapt.city_profile':
                append_urls(obj.website_of_the_local_authority, path)
        attrs = ['long_description', 'description', 'source', 'comments']
        for attr in attrs:
            string_to_search = convert_to_string(getattr(obj, attr, ''))

            if len(string_to_search) > 0:
                if attr == 'long_description':
                    bs = BeautifulSoup(string_to_search)
                    links = bs.findAll(
                        'a', attrs={'href': re.compile("^https?://")}
                    )

                    for link in links:
                        append_urls(link.get('href'), path)
                else:
                    links = discover_links(string_to_search)

                    # get rid of duplicates
                    links = list(set(links))
                    for link in links:
                        append_urls(link, path)

        if obj.portal_type == 'collective.cover.content':
            for tile in obj.list_tiles():
                if 'richtext' in obj.get_tile_type(tile):
                    richtext = obj.get_tile(tile).getText()
                    bs = BeautifulSoup(richtext)
                    links = bs.findAll(
                        'a', attrs={'href': re.compile("^https?://")}
                    )
                    for link in links:
                        append_urls(link.get('href'), path)

        count += 1
        if count % 100 == 0:
            logger.info('Finished going through %s objects' % count)

    logger.info("Finished getting links.")
    return urls


def check_link(link):
    """ Check the links and return only the broken ones with the respective
        status codes
    """

    if link:
        if isinstance(link, unicode):
            link = link.encode()

        try:
            if link[0:7].find('http') == -1:
                link = 'http://' + link
        except Exception, err:
            logger.error(err)

        logger.info("LINK: %s", link)
        try:
            requests.head(link, timeout=5, allow_redirects=True)
        except requests.exceptions.ReadTimeout:
            return {'status': '504', 'url': link}
        except requests.exceptions.ConnectTimeout:
            logger.info("Timed out.")
            logger.info("Trying again with link: %s", link)
            try:
                requests.head(link, timeout=30, allow_redirects=True)
            except:
                return {'status': '504', 'url': link}
        except requests.exceptions.TooManyRedirects:
            logger.info("Redirected.")
            logger.info("Trying again with link: %s", link)
            try:
                requests.head(link, timeout=30, allow_redirects=True)
            except:
                return {'status': '301', 'url': link}
        except requests.exceptions.URLRequired:
            return {'status': '400', 'url': link}
        except requests.exceptions.ProxyError:
            return {'status': '305', 'url': link}
        except requests.exceptions.HTTPError:
            return {'status': '505', 'url': link}
        except:
            return {'status': '404', 'url': link}

    return
