# -*- coding: utf-8 -*-
""" Module where all interfaces, events and exceptions live. """

from eni.seis.content.config import REPORTS_STATUS_VOCAB
from eni.seis.content.config import UNECE_INDICATORS_CATEGORIES_VOCAB
from eni.seis.content.config import UNECE_INDICATORS_SUBCATEGORIES_VOCAB
from eni.seis.content.vocabulary import EAST_LANGUAGES_VOCABULARY
from eni.seis.content.vocabulary import EAST_PRODUCTS_CATEGORIES_VOCABULARY
from eni.seis.content.vocabulary import EAST_YEARS_VOCABULARY
from plone.app.textfield import RichText
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone.autoform import directives as form
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.form.browser.select import SelectWidget
from zope import schema
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


class INationalReport(model.Schema):
    """ National Report item to be added in a country section
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

    pages_number = schema.TextLine(
        title=u"Number of pages",
        required=False,
        description=u"Example: 171"
    )

    languages = schema.List(
        title=u"Languages",
        description=u"Select available languages for this report.",
        required=False,
        value_type=schema.Choice(source=EAST_LANGUAGES_VOCABULARY),
    )

    years = schema.List(
        title=u"Years",
        description=u"Years reported for",
        required=False,
        value_type=schema.Choice(source=EAST_YEARS_VOCABULARY),
    )


class IProductItem(model.Schema):
    """ ProductItem to be added in a country section
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

    product_category = schema.Choice(
        title=u"Category",
        description=u"Select the category.",
        required=True,
        vocabulary=EAST_PRODUCTS_CATEGORIES_VOCABULARY,
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


class IIndicatorData(model.Schema):
    """ IndicatorData item
    """
    long_description = RichText(
        title=u"Long description",
        required=False,
    )

    image = NamedBlobImage(
        title=u"Lead image",
        required=False,
    )

    key_messages = RichText(
        title=u"Key messages",
        required=False,
    )

    text_before = RichText(
        title=u"Body text (section before figures)",
        required=False,
    )

    text = RichText(
        title=u"Body text (section after figures)",
        required=False,
    )

    topics = schema.List(
        title=u'Topics',
        required=False,
        value_type=schema.TextLine(title=u'Topic', default=u"")
    )

    indicator_code = schema.TextLine(
        title=u'Indicator code',
        required=False,
    )

    temporal_coverage = schema.TextLine(
        title=u'Temporal coverage',
        required=False,
        # TODO ? fix field type
    )

    dpsir = schema.TextLine(
        title=u'DPSIR',
        required=False,
    )

    typology = schema.TextLine(
        title=u'Typology',
        required=False,
    )

    contact = RichText(
        title=u'Contact',
        required=False,
    )

    ownership = RichText(
        title=u'Ownership',
        required=False,
    )

    related_content = RichText(
        title=u'Related content',
        required=False,
    )

    frecvency_of_updates = schema.TextLine(
        title=u'Frecvency of updates',
        required=False,
    )

    dashboards_heights = schema.TextLine(
        title=u'Dashboards heights',
        description=u'Example: 600, 680 - will set the height for 1st and 2nd',
        required=False,
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


class INewsletter(model.Schema):
    """ newsletter item
    """
    photo = NamedBlobImage(
        title=u"Photo",
        required=True,
    )

    link = schema.URI(
        title=u"Internal or External link",
        required=False,
        description=u"The source for your newsletter item."
    )

    file = NamedBlobFile(
        title=u"File",
        required=False,
        description=u"If you prefer you can upload the file right here. " +
        "Let the link field empty in this case."
    )
