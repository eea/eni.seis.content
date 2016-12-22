from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from zope.schema import Choice, Tuple


@provider(IFormFieldProvider)
class ICountries(model.Schema):

    # model.fieldset(
    #     'countries',
    #     label=u'Countries',
    #     fields=('countries',),
    # )

    directives.widget('countries', CheckBoxFieldWidget)
    countries = Tuple(
        title=u"Countries",
        description=u"Relevant countries",
        required=True,
        default=(),
        value_type=Choice(
            title=u"Country",
            vocabulary="european_countries",
        )
    )


@implementer(ICountries)
@adapter(IDexterityContent)
class Countries(object):
    """
    """

    def __init__(self, context):
        self.context = context

    @property
    def countries(self):
        return getattr(self.context, 'countries', None)

    @countries.setter
    def countries(self, value):
        if value is None:
            value = ()
        self.context.countries = value
        self.context._p_changed = True
