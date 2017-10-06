# -*- coding: utf-8 -*-
from eni.seis.content.config import MessageFactory as _
from plone.dexterity.browser import edit
from plone.dexterity.interfaces import IDexterityEditForm
from plone.z3cform import layout
from zope.interface import classImplements
from plone.z3cform.fieldsets.extensible import FormExtender
from z3c.form.field import Fields
from z3c.form import util
from zope import schema


class EditFormExtender(FormExtender):
    def update(self):
        if self.request.REQUEST_METHOD == 'GET':
            # add fields
            subscriber = self.context
            details = subscriber.get_details()
            phones = details.get("phone_numbers", "")
            if phones == "":
                phones = []

            first_name = schema.TextLine(
                __name__="first_name",
                title=_(u'label_first_name', default=u'Name'),
                description=_(u'help_first_name',
                              default=u'Enter your first name.'),
                required=False,
                default=util.toUnicode(details.get("first_name", ""))
            )

            last_name = schema.TextLine(
                __name__="last_name",
                title=_(u'label_last_name', default=u'Surname'),
                description=_(u'help_last_name',
                              default=u'Enter your last name (family name).'),
                required=False,
                default=util.toUnicode(details.get("last_name", ""))
            )

            phone_numbers = schema.List(
                __name__="phone_numbers",
                title=_(u'label_phone_numbers', default=u'Phone numbers'),
                description=_(u'help_phone_numbers',
                              default=u'Fill in phone numbers.'),
                value_type=schema.TextLine(),
                required=False,
                default=phones
            )

            institution = schema.TextLine(
                __name__="institution",
                title=_(u'label_institution', default=u'Institution'),
                description=_(u'help_institution',
                              default=u'Fill in the institution'),
                required=False,
                default=util.toUnicode(details.get("institution", ""))
            )

            position = schema.TextLine(
                __name__="position",
                title=_(u'label_position', default=u'Position'),
                description=_(u'help_position',
                              default=u'Fill in the position'),
                required=False,
                default=util.toUnicode(details.get("position", ""))
            )

            from_country = schema.TextLine(
                __name__="from_country",
                title=_(u'label_from_country', default=u'From country'),
                description=_(u'help_from_country',
                              default=u'Fill in the From country'),
                required=False,
                default=util.toUnicode(details.get("from_country", ""))
            )

            from_city = schema.TextLine(
                __name__="from_city",
                title=_(u'label_from_city', default=u'From city'),
                description=_(u'help_from_city',
                              default=u'Fill in the From city'),
                required=False,
                default=util.toUnicode(details.get("from_city", ""))
            )

            address = schema.Text(
                __name__="address",
                title=_(u'label_address', default=u'Address'),
                description=_(u'help_address',
                              default=u'Fill in the address'),
                required=False,
                default=util.toUnicode(details.get("address", ""))
            )

            self.form.fields += Fields(
                first_name, last_name, phone_numbers,
                institution, position, from_country, from_city, address)

        if self.request.REQUEST_METHOD == 'POST':
            # save values
            # [TODO] Update only if the entire form was submitted.
            # [TODO] Update user profile with these values.
            prefix = 'form.widgets.'
            field_names = [
                'first_name', 'last_name', 'telephone',
                'phone_numbers', 'institution', 'position', 'from_country',
                'from_city', 'address']

            print "UPDATED:"
            for field_name in field_names:
                print self.request.form.get(prefix + field_name)


class EditForm(edit.DefaultEditForm):
    """ Override meeting subscriber edit form to add fields
    """


EditView = layout.wrap_form(EditForm)
classImplements(EditView, IDexterityEditForm)
