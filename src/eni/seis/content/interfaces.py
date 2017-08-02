# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from eni.seis.content.config import REPORTS_TYPES_VOCAB
from eni.seis.content.config import UNECE_INDICATORS_CATEGORIES_VOCAB
from eni.seis.content.config import UNECE_INDICATORS_SUBCATEGORIES_VOCAB
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope import schema


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


class IReport(model.Schema):
    """ Report item to be added in a country section
    """
    external_link = schema.URI(
        title=u"External link",
        required=False,
        description=u"Report source if it is an external link."
    )

    file = NamedBlobFile(
        title=u"File",
        required=False,
        description=u"Report file if it has one."
    )

    report_type = schema.Choice(
        title=u"Type of the report",
        vocabulary=REPORTS_TYPES_VOCAB,
        required=True
        )


class IIndicator(model.Schema):
    """ Indicator item to be added in a country section
    """
    external_link = schema.URI(
        title=u"External link",
        required=False,
        description=u"Indicator source if it is an external link."
    )

    file = NamedBlobFile(
        title=u"File",
        required=False,
        description=u"Indicator file if it has one."
    )

    category = schema.Choice(
        title=u"Category",
        vocabulary=UNECE_INDICATORS_CATEGORIES_VOCAB,
        required=True
        )

    subcategory = schema.Choice(
        title=u"Subcategory",
        vocabulary=UNECE_INDICATORS_SUBCATEGORIES_VOCAB,
        required=True
        )
