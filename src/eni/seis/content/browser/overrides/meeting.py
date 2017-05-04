from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import plone.api as api

from eea.meeting.browser import views


FIELDS_REGISTRATION = (
    ('first_name', 'first_name'),
    ('last_name', 'last_name'),
    ('position', 'position'),
    ('organisation', 'institution'),
    ('address', 'address'),
    ('country', 'from_country'),
    ('email', 'email'),
    ('phone_numbers', 'phone_numbers'),
)


class Register(views.Register):
    index = ViewPageTemplateFile('meeting_register.pt')

    def __call__(self):
        if self.request.method == 'POST':
            if 'submit.login' in self.request:
                return self.login()
            elif 'submit.register' in self.request:
                return self.register()

        elif api.user.is_anonymous():
            return self.index()

        return super(Register, self).__call__()

    def login(self):
        name = self.request.get('__ac_name')
        pwd = self.request.get('__ac_password')
        portal = api.portal.get()
        acl = portal.acl_users
        user = acl.authenticate(name, pwd, self.request)

        if user is not None:
            api.portal.show_message(
                'Login successful.', request=self.request, type='info')
            acl.session._setupSession(user.getId(), self.request.response)
            return self.request.response.redirect(
                self.context.absolute_url() + '/register'
            )

        api.portal.show_message(
            'Invalid credentials.', request=self.request, type='error')
        return self.index()

    def register(self):
        pw1, pw2 = self.request.get('pw1'), self.request.get('pw2')
        if pw1 != pw2:
            return self.index()

        member_data = {
            member_key: self.request.get(form_key)
            for form_key, member_key in FIELDS_REGISTRATION
        }

        member_data['fullname'] = '{} {}'.format(
            member_data['first_name'],
            member_data['last_name'],
        )

        member = api.user.create(
            email=self.request.get('email'),
            username=self.request.get('username'),
            password=pw1,
            properties=member_data,
        )

        acl = api.portal.get().acl_users
        acl.session._setupSession(member.getId(), self.request.response)
        return self.request.response.redirect(
            self.context.absolute_url() + '/register'
        )
