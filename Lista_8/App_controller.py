from Covid_serv import Covid_service


class App_controller:
    def __init__(self):
        self.covid_service = Covid_service()
        self.covid_service.make_data()

    def deaths_world(self, date_day=None, date_month=None):
        if date_day is None and date_month is None:
            return self.covid_service.get_world_sum()[1]
        if date_day is None:
            return self.covid_service.get_world_month(date_month)[1]
        return self.covid_service.get_world_day(date_day, date_month)[1]

    def cases_world(self, date_day=None, date_month=None):
        if date_day is None and date_month is None:
            return self.covid_service.get_world_sum()[0]
        if date_day is None:
            return self.covid_service.get_world_month(date_month)[0]
        return self.covid_service.get_world_day(date_day, date_month)[0]

    def deaths_continent(self, continent_name, date_day=None, date_month=None):
        if date_day is None and date_month is None:
            return self.covid_service.get_continent_deaths(continent_name)
        if date_day is None:
            return self.covid_service.get_continent_month_deaths(continent_name, month_name=date_month)
        return self.covid_service.get_continent_day_deaths(continent_name, day=date_day, month_name=date_month)

    def cases_continent(self, continent_name, date_day=None, date_month=None):
        if date_day is None and date_month is None:
            return self.covid_service.get_continent_cases(continent_name)
        if date_day is None:
            return self.covid_service.get_continent_month_cases(continent_name, month_name=date_month)
        return self.covid_service.get_continent_day_cases(continent_name, day=date_day, month_name=date_month)

    def deaths_country(self, country_name, date_day=None, date_month=None):
        if date_day is None and date_month is None:
            return self.covid_service.get_country_deaths(country_name)
        if date_day is None:
            return self.covid_service.get_country_month_deaths(country_name, month_name=date_month)
        return self.covid_service.get_country_day_deaths(country_name, day=date_day, month_name=date_month)

    def cases_country(self, country_name, date_day=None, date_month=None):
        if date_day is None and date_month is None:
            return self.covid_service.get_country_cases(country_name)
        if date_day is None:
            return self.covid_service.get_country_month_cases(country_name, month_name=date_month)
        return self.covid_service.get_country_day_cases(country_name, day=date_day, month_name=date_month)

