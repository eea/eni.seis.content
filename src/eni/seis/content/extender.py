from archetypes.schemaextender.interfaces import ISchemaExtender
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import TextField
from Products.ATContentTypes.interfaces import IATFolder
from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.field import ExtensionField


class ExtensionTextField(ExtensionField, TextField):
    """ derivative of stringfield for extending schemas """


class DescriptionFieldExtender(object):

    adapts(IATFolder)
    implements(ISchemaExtender)

    _fields = [

        ExtensionTextField(
            'long_description',
            required=False,
            schemata='default',
            searchable=True,
            primary=False,
            default_output_type='text/x-html-safe',
            widget=RichWidget(
                description='',
                label='Body Text',
                rows=25,
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self._fields
