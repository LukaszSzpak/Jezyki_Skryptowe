from Covid_serv import Covid_service


class App_controller:
    def __init__(self):
        self.covid_service = Covid_service()
        self.covid_service.make_data()

    def deaths_world(self, date=None):
        if date is None:
            return self.covid_service.get_world_sum()[1]

    def cases_world(self, date=None):
        if date is None:
            return self.covid_service.get_world_sum()[0]

    def deaths_continent(self, continent_name, date=None):
        if date is None:
            return self.covid_service.get_continent_deaths(continent_name)

    def cases_continent(self, continent_name, date=None):
        if date is None:
            return self.covid_service.get_continent_cases(continent_name)

    def deaths_country(self, country_name, date=None):
        if date is None:
            return self.covid_service.get_country_deaths(country_name)

    def cases_country(self, country_name, date=None):
        if date is None:
            return self.covid_service.get_country_cases(country_name)

