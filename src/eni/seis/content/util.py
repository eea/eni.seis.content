from plone import api
from plone.dexterity.interfaces import IDexterityContent
from Products.PythonScripts.standard import url_quote
import re
import string


def portal_absolute_url():
    return api.portal.get().absolute_url()


def reduce_text(text, limit):
    text = re.sub('<[^<]+?>', '', text)
    if len(text) <= limit:
        return text
    new_text = text[:limit]
    new_text_split = new_text.split(' ')
    slice_size = -1 if len(new_text_split) > 1 else 1
    clean_text = ' '.join(new_text_split[:slice_size])

    if clean_text[-1] in string.punctuation:
        clean_text = clean_text[:-1]

    return '{0}...'.format(clean_text)


class Text(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        if isinstance(self.text, unicode):
            return self.text.encode('utf-8')
        else:
            return self.text

    def __unicode__(self):
        if isinstance(self.text, str):
            return self.text.decode('utf-8')
        else:
            return self.text

    def trim(self, limit=150):
        return reduce_text(self.text, limit)


def field_value(obj, field_name):
    if IDexterityContent.providedBy(obj):
        try:
            return getattr(obj, field_name).raw
        except AttributeError:
            return getattr(obj, field_name)
    else:
        field = obj.getField(field_name)
        if field:
            return field.getAccessor(obj)()


class Tag(object):
    def __init__(self, tag):
        self.tag = tag

    @property
    def url(self):
        url = '{0}/@@search?Subject%3Alist={1}'.format(
            api.portal.get().absolute_url(),
            url_quote(self.tag)
        )
        return url

    @property
    def title(self):
        return self.tag


class ItemUtil(object):
    def __init__(self, brain=None, obj=None):
        if brain is not None:
            self.brain = brain
            self.obj = brain.getObject()
        elif obj is not None:
            self.obj = obj

    def field_value(self, field_name):
        return field_value(self.obj, field_name)

    @property
    def title(self):
        return Text(self.obj.title_or_id())

    @property
    def url(self):
        return self.obj.absolute_url()

    @property
    def description(self):
        return Text(self.field_value('description'))

    def get_image_url(self, field_name, width, height, direction='down'):
        scales = self.obj.restrictedTraverse('@@images')
        try:
            image = scales.scale(
                field_name,
                width=width, height=height,
                direction=direction
            )
        except TypeError:
            image = None
        if image is not None:
            return image.url

    @property
    def tags(self):
        for tag in self.obj.Subject():
            yield Tag(tag)

    @property
    def css_portal_type(self):
        return '-'.join(self.obj.portal_type.lower().split())


class EventItem(ItemUtil):

    @property
    def type(self):
        return self.field_value('event_type')

    @property
    def location(self):
        return self.field_value('location')

    @property
    def date(self):
        date = self.field_value('startDate')
        if date:
            return date.asdatetime().strftime('%B %d, %Y')

    @property
    def start_date(self):
        date = self.field_value('startDate')
        return {
            'month': date.Month(),
            'day': date.day(),
            'year': date.year()
        }

    @property
    def month(self):
        return self.start_date.get('month')

    @property
    def day(self):
        return self.start_date.get('day')

    @property
    def year(self):
        return self.start_date.get('year')

    @property
    def image_url(self):
        return self.get_image_url('logo', 200, 100)
