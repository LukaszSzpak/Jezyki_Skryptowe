from Covid_serv import Covid_service


class App_controller:
    def __init__(self):
        self.covid_service = Covid_service()

    def deaths_world(self, date=None):
        pass

    def cases_world(self, date=None):
        pass

    def deaths_continent(self, continent_name, date=None):
        pass

    def cases_continent(self, continent_name, date=None):
        pass

    def deaths_country(self, country_name, date=None):
        pass

    def cases_country(self, country_name, date=None):
        pass

