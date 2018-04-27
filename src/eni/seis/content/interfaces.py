# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from eni.seis.content.config import REPORTS_STATUS_VOCAB
from eni.seis.content.config import UNECE_INDICATORS_CATEGORIES_VOCAB
from eni.seis.content.config import UNECE_INDICATORS_SUBCATEGORIES_VOCAB
from plone.autoform import directives as form
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
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
        vocabulary="environmental_assesment_reports_types",
        required=True
        )

    status = schema.Choice(
        title=u"Status",
        vocabulary=REPORTS_STATUS_VOCAB,
        required=True
        )

    status_details = schema.TextLine(
        title=u"Status details",
        required=False,
        description=u"Example: Annual"
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


class INationalFocalPoint(model.Schema):
    """ nfp item to be added in a country section
    """
    form.widget('name', WysiwygFieldWidget)
    name = schema.Text(
        title=u"Name",
        required=True,
    )

    form.widget('organisation', WysiwygFieldWidget)
    organisation = schema.Text(
        title=u"Organisation",
        required=True,
    )

    form.widget('position', WysiwygFieldWidget)
    position = schema.Text(
        title=u"Position",
        required=True,
    )

    photo = NamedBlobImage(
        title=u"Photo",
        required=False,
    )
