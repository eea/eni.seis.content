# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IEniSeisContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IEniSeisEastContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer.
       Used for EAST website.
    """


class IEniSeisSouthContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer.
       Used for SOUTH website.
    """
