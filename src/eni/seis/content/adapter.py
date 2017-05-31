from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    @property
    def first_name(self):
        value = self.context.getProperty('first_name', '')
        return value.decode('utf-8')

    @first_name.setter
    def first_name(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'first_name': value.encode('utf-8')})

    @property
    def last_name(self):
        value = self.context.getProperty('last_name', '')
        return value.decode('utf-8')

    @last_name.setter
    def last_name(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'last_name': value.encode('utf-8')})

    @property
    def telephone(self):
        value = self.context.getProperty('telephone', '')
        return value.decode('utf-8')

    @telephone.setter
    def telephone(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'telephone': value.encode('utf-8')})

    @property
    def phone_numbers(self):
        value = self.context.getProperty('phone_numbers', [])
        return [v.decode('utf-8') for v in value]

    @phone_numbers.setter
    def phone_numbers(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'phone_numbers': [v.encode('utf-8') for v in value]})

    @property
    def institution(self):
        value = self.context.getProperty('institution', '')
        return value.decode('utf-8')

    @institution.setter
    def institution(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'institution': value.encode('utf-8')})

    @property
    def position(self):
        value = self.context.getProperty('position', '')
        return value.decode('utf-8')

    @position.setter
    def position(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'position': value.encode('utf-8')})

    @property
    def from_country(self):
        value = self.context.getProperty('from_country', '')
        return value.decode('utf-8')

    @from_country.setter
    def from_country(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'from_country': value.encode('utf-8')})

    @property
    def from_city(self):
        value = self.context.getProperty('from_city', '')
        return value.decode('utf-8')

    @from_city.setter
    def from_city(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'from_city': value.encode('utf-8')})

    @property
    def address(self):
        value = self.context.getProperty('address', '')
        return value.decode('utf-8')

    @address.setter
    def address(self, value):
        if value is not None:
            return self.context.setMemberProperties(
                {'address': value.encode('utf-8')})
