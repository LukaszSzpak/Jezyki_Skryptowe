from Covid_serv import Covid_service
import operator
from itertools import islice


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

    def check_location_and_get_deaths(self, location, date_day=None, date_month=None):
        try:
            if location == 'swiat':
                return self.deaths_world(date_day=date_day, date_month=date_month)

            if self.covid_service.is_it_country(location):
                return self.deaths_country(country_name=location, date_month=date_month, date_day=date_day)

            if self.covid_service.is_it_continent(location):
                return self.deaths_continent(continent_name=location, date_month=date_month, date_day=date_day)

            return 'Bledna lokalizacja !'
        except:
            return 'Data niedostępna !'

    def check_location_and_get_cases(self, location, date_day=None, date_month=None):
        try:
            if date_month is not None:
                if not self.covid_service.is_it_month(date_month):
                    return 'Bledny miesiac !'

            if location == 'swiat':
                return self.cases_world(date_day=date_day, date_month=date_month)

            if self.covid_service.is_it_country(location):
                return self.cases_country(country_name=location, date_month=date_month, date_day=date_day)

            if self.covid_service.is_it_continent(location):
                return self.cases_continent(continent_name=location, date_month=date_month, date_day=date_day)

            return 'Bledna lokalizacja !'
        except:
            return 'Data niedostępna !'

    def get_max_cases(self, number_of_days):
        get_dict = self.covid_service.get_world_dates()
        sorted_dict = sorted(get_dict.items(), key=lambda day: day[1].get_cases(), reverse=True)

        str = ''
        for date, day in islice(sorted_dict, number_of_days):
            str += '{0}: zachorowania: {1} \n'.format(date, day.get_cases())
        return str

    def get_max_deaths(self, number_of_days):
        get_dict = self.covid_service.get_world_dates()
        sorted_dict = sorted(get_dict.items(), key=lambda day: day[1].get_deaths(), reverse=True)

        str = ''
        for date, day in islice(sorted_dict, number_of_days):
            str += '{0}: zgony: {1} \n'.format(date, day.get_deaths())
        return str
