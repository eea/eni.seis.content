from zope.component.hooks import getSite


def autofillFullname(event):
    """ Because we splitted user fullname in first_name and last_name on
        register, fullname was omited from schema. But we autofill this
        on register event.
    """
    site = getSite()
    first_name = site.REQUEST.form.get('form.first_name', '')
    last_name = site.REQUEST.form.get('form.last_name', '')
    # This event might not be triggered by the
    # default Plone form (e.g. api.user.create).
    if first_name or last_name:
        auto_fullname = first_name + " " + last_name
        principal = event.principal
        properties = principal._propertysheets.get('mutable_properties')
        properties.setProperty(principal, 'fullname', auto_fullname)


def set_folder_listing_by_default(folder, event):
    """ Set folder_listing as default Display for new created folders.
        This solves the problem: country_view_east as default Display
        for new folders added in East countries folders, for example.

        But skip this action for Folderish Event, News Item and Page.
        """
    if 'Folderish' not in folder.portal_type:
        folder.setLayout('folder_listing')
