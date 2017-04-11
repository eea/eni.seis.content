from zope.component.hooks import getSite


def autofillFullname(event):
    """ Because we splitted user fullname in first_name and last_name on
        register, fullname was omited from schema. But we autofill this
        on register event.
    """
    site = getSite()
    first_name = site.REQUEST.form.get('form.first_name')
    last_name = site.REQUEST.form.get('form.last_name')
    auto_fullname = first_name + " " + last_name
    principal = event.principal
    properties = principal._propertysheets.get('mutable_properties')
    properties.setProperty(principal, 'fullname', auto_fullname)