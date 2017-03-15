from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_first_name(self):
        first_name = self.context.getProperty('first_name', '').decode('utf-8')
        return first_name

    def set_first_name(self, value):
        first_name = value
        return self.context.setMemberProperties(
            {'first_name': first_name.encode('utf-8')})
    first_name = property(get_first_name, set_first_name)

    def get_last_name(self):
        last_name = self.context.getProperty('last_name', '').decode('utf-8')
        return last_name

    def set_last_name(self, value):
        last_name = value
        return self.context.setMemberProperties(
            {'last_name': last_name.encode('utf-8')})
    last_name = property(get_last_name, set_last_name)

    def get_telephone(self):
        return self.context.getProperty('telephone', '').decode('utf-8')

    def set_telephone(self, value):
        return self.context.setMemberProperties(
            {'telephone': value.encode('utf-8')})
    telephone = property(get_telephone, set_telephone)

    def get_institution(self):
        return self.context.getProperty('institution', '').decode('utf-8')

    def set_institution(self, value):
        return self.context.setMemberProperties(
            {'institution': value.encode('utf-8')})
    institution = property(get_institution, set_institution)

    def get_from_country(self):
        return self.context.getProperty('from_country', '').decode('utf-8')

    def set_from_country(self, value):
        return self.context.setMemberProperties(
            {'from_country': value.encode('utf-8')})
    from_country = property(get_from_country, set_from_country)

    def get_from_city(self):
        return self.context.getProperty('from_city', '').decode('utf-8')

    def set_from_city(self, value):
        return self.context.setMemberProperties(
            {'from_city': value.encode('utf-8')})
    from_city = property(get_from_city, set_from_city)
