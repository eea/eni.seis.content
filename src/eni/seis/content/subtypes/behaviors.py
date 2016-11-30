from Products.CMFCore.interfaces import IDublinCore
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer, Interface
from zope.interface import provider
from zope.schema import Choice


class ICountries(model.Schema):

    # directives.fieldset(
    #     'categorization',
    #     label=_(u'Categorization'),
    #     fields=('tags',),
    # )

    countries = Choice(
        title=u"Countries",
        description=u"Applicable countries",
        required=True,
        vocabulary="european_countries",
    )


@implementer(ICountries)
@adapter(IDexterityContent)
class Countries(object):
    """
    """

    def __init__(self, context):
        selft.context = context

    @property
    def countries(self):
        return getattr(self.context, 'countries', None)

    @countries.setter
    def countries(self, value):
        if value is None:
            value = ()
        self.context.countries = value
        self.context._p_changed = True
