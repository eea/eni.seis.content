from zope.component import getUtility
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.browser.register import RegistrationForm
from plone.app.users.browser.register import CantChoosePasswordWidget
from Products.CMFCore.interfaces import ISiteRoot
from zope import schema
from zope.interface import implements
from eni.seis.content.config import MessageFactory as _


class EniRegistrationForm(RegistrationForm):

    @property
    def form_fields(self):
        if not self.showForm:
            # We do not want to spend time calculating fields that
            # will never get displayed.
            return []
        portal = getUtility(ISiteRoot)
        defaultFields = super(RegistrationForm, self).form_fields
        # Can the user actually set his/her own password?
        if portal.getProperty('validate_email', True):
            # No? Remove the password fields.
            defaultFields = defaultFields.omit('password', 'password_ctl')
            # Show a message indicating that a password reset link
            # will be mailed to the user.
            defaultFields['mail_me'].custom_widget = CantChoosePasswordWidget
        else:
            # The portal is not interested in validating emails, and
            # the user is not interested in getting an email with a
            # link to set his password if he can set this password in
            # the current form already.
            defaultFields = defaultFields.omit('mail_me')

        defaultFields = defaultFields.omit('fullname')

        return defaultFields


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    first_name = schema.TextLine(
        title=_(u'label_first_name', default=u'Name'),
        description=_(u'help_first_name',
                      default=u'Enter your first name.'),
        required=True,
    )

    last_name = schema.TextLine(
        title=_(u'label_last_name', default=u'Surname'),
        description=_(u'help_last_name',
                      default=u'Enter your last name (family name).'),
        required=True,
    )

    telephone = schema.TextLine(
        title=_(u'label_telephone', default=u'Phone number'),
        description=_(u'help_telephone',
                      default=u'Fill in the phone number'),
        required=False
    )

    phone_numbers = schema.List(
        title=_(u'label_phone_numbers', default=u'Phone numbers'),
        description=_(u'help_phone_numbers',
                      default=u'Fill in phone numbers.'),
        value_type=schema.TextLine(),
        required=False
    )

    institution = schema.TextLine(
        title=_(u'label_institution', default=u'Institution'),
        description=_(u'help_institution',
                      default=u'Fill in the institution'),
        required=True,
    )

    position = schema.TextLine(
        title=_(u'label_position', default=u'Position'),
        description=_(
            u'help_position',
            default=u'Fill in your position within your Institution'),
        required=True,
    )

    from_country = schema.TextLine(
        title=_(u'label_from_country', default=u'From country'),
        description=_(u'help_from_country',
                      default=u'Fill in the From country'),
        required=True,
    )

    from_city = schema.TextLine(
        title=_(u'label_from_city', default=u'From city'),
        description=_(u'help_from_city',
                      default=u'Fill in the From city'),
        required=False,
    )

    address = schema.Text(
        title=_(u'label_address', default=u'Address'),
        description=_(u'help_address',
                      default=u'Fill in the address'),
        required=True,
    )
