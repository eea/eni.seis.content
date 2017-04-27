from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_first_name(self):
        value = self.context.getProperty('first_name', '')
        if value is not None:
            value = value.decode('utf-8')
        return value

    def set_first_name(self, value):
        if value is not None:
            value = value.encode('utf-8')
        return self.context.setMemberProperties(
            {'first_name': value})
    first_name = property(get_first_name, set_first_name)

    def get_last_name(self):
        value = self.context.getProperty('last_name', '')
        if value is not None:
            value = value.decode('utf-8')
        return value

    def set_last_name(self, value):
        if value is not None:
            value = value.encode('utf-8')
        return self.context.setMemberProperties(
            {'last_name': value})
    last_name = property(get_last_name, set_last_name)

    def get_telephone(self):
        value = self.context.getProperty('last_name', '')
        if value is not None:
            value = value.decode('utf-8')
        return value

    def set_telephone(self, value):
        if value is not None:
            value = value.encode('utf-8')
        return self.context.setMemberProperties(
            {'telephone': value})
    telephone = property(get_telephone, set_telephone)

    def get_institution(self):
        value = self.context.getProperty('institution', '')
        if value is not None:
            value = value.decode('utf-8')
        return value

    def set_institution(self, value):
        if value is not None:
            value = value.encode('utf-8')
        return self.context.setMemberProperties(
            {'institution': value})
    institution = property(get_institution, set_institution)

    def get_from_country(self):
        value = self.context.getProperty('from_country', '')
        if value is not None:
            value = value.decode('utf-8')
        return value

    def set_from_country(self, value):
        if value is not None:
            value = value.encode('utf-8')
        return self.context.setMemberProperties(
            {'from_country': value})
    from_country = property(get_from_country, set_from_country)

    def get_from_city(self):
        value = self.context.getProperty('from_city', '')
        if value is not None:
            value = value.decode('utf-8')
        return value

    def set_from_city(self, value):
        if value is not None:
            value = value.encode('utf-8')
        return self.context.setMemberProperties(
            {'from_city': value})
    from_city = property(get_from_city, set_from_city)
