from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import plone.api as api

from eea.meeting.browser import views


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
