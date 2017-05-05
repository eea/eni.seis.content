from functools import partial
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

FIELDS_REQUIRED = (
    ('first_name', 'First name'),
    ('last_name', 'Last name'),
    ('position', 'Position'),
    ('organisation', 'Organisation'),
    ('username', 'Username'),
    ('email', 'Email'),
    ('pw1', 'Password'),
)


def create_user(request):
    member_data = {
        member_key: request.get(form_key)
        for form_key, member_key in FIELDS_REGISTRATION
    }

    member_data['fullname'] = '{} {}'.format(
        member_data['first_name'],
        member_data['last_name'],
    )

    return api.user.create(
        email=request.get('email'),
        username=request.get('username'),
        password=request.get('pw1'),
        properties=member_data,
    )


def login_user(response, user):
    acl = api.portal.get().acl_users
    acl.session._setupSession(user.getId(), response)


def check_pw(request):
    pw1, pw2 = request.get('pw1'), request.get('pw2')
    return pw1 == pw2 or 'Passwords do not match!'


def check_required(request):
    missing_fields = [
        label for fname, label in FIELDS_REQUIRED
        if not request.get(fname)
    ]

    if missing_fields:
        return (
            'These fields are required: {}!'
            .format(', '.join(missing_fields))
        )


REGISTER_VALIDATORS = (
    check_pw,
    check_required,
)


def register_error(request, template, msg):
    return template(
        register_message={'type': 'error', 'text': msg},
        fields={
            form_key: request.get(form_key)
            for form_key, _ in FIELDS_REGISTRATION
        }
    )


class Register(views.Register):
    index = ViewPageTemplateFile('meeting_register.pt')

    def __call__(self):
        self.is_anon = api.user.is_anonymous()
        self.response = self.request.response

        if self.request.method == 'POST':
            if 'submit.login' in self.request:
                return self.login()
            elif 'submit.register' in self.request:
                return self.register()

        if not self.is_anon:
            if self.request.get('login'):
                return self.index(
                    login_message={
                        'type': 'good',
                        'text': 'Login successful!'
                    }
                )
            elif self.request.get('created'):
                return self.index(
                    created_message={
                        'type': 'good',
                        'text': 'User account created!',
                    }
                )

        return self.index()

    def login(self):
        name = self.request.get('__ac_name')
        pwd = self.request.get('__ac_password')
        portal = api.portal.get()
        acl = portal.acl_users
        user = acl.authenticate(name, pwd, self.request)

        if user is not None:
            login_user(self.response, user)
            return self.response.redirect(
                self.context.absolute_url() + '/register?login=true')

        return self.index(
            login_message={'type': 'error', 'text': 'Invalid credentials!'}
        )

    def register(self):
        err_msg = partial(register_error, self.request, self.index)

        def reducer(acc, cur):
            return '\n'.join((acc, cur)) if type(cur) == str else acc

        errors = reduce(reducer, (
            name(self.request)
            for name in REGISTER_VALIDATORS
        ) , '')
        if errors:
            return err_msg(errors)

        try:
            login_user(self.response, create_user(self.request))
        except Exception as e:
            return err_msg(e.message)

        return self.response.redirect(
            self.context.absolute_url() + '/register?created=true')
