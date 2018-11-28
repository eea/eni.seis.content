""" Just restore the original viewlet to solve the issue of multiple warnings:
        WARNING eea.versions.versions DefaultView: Object http://... has
        different version id than its default view

    So, instead of this (we don't use eea.versions):
    https://github.com/eea/eea.versions/blob/master/eea/versions/browser/
                                                                 overrides.zcml

    use orginal code:
    https://github.com/plone/plone.app.layout/blob/master/plone/app/layout/
                                                              links/viewlets.py
"""

# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase
from plone.memoize import view
from zope.component import getMultiAdapter


class CanonicalURL(ViewletBase):
    """Defines a canonical link relation viewlet to be displayed across the
    site. A canonical page is the preferred version of a set of pages with
    highly similar content. For more information, see:
    https://tools.ietf.org/html/rfc6596
    https://support.google.com/webmasters/answer/139394?hl=en
    """

    @view.memoize
    def render(self):
        context_state = getMultiAdapter(
            (self.context, self.request), name=u'plone_context_state')
        canonical_url = context_state.canonical_object_url()
        return u'    <link rel="canonical" href="%s" />' % canonical_url
