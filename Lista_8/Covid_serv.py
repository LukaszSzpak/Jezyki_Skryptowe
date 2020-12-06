from itertools import islice
from Name_data import Name_data

FILE_PATH = "Covid19.txt"


class Covid_service:
    __month_dict = {'styczeń': '01',
                  'luty': '02',
                  'marzec': '03',
                  'kwiecień': '04',
                  'maj': '05',
                  'czerwiec': '06',
                  'lipiec': '07',
                  'sierpień': '08',
                  'wrzesień': '09',
                  'październik': '10',
                  'listopad': '11',
                  'grudzień': '12'}

    def __init__(self):
        self.__file = open(FILE_PATH, 'r')
        self.__country_dict = {}
        self.__continent_dict = {}

    def __add_to_country(self, country_name, date, cases, deaths):
        if country_name in self.__country_dict:
            self.__country_dict[country_name].add(date, cases, deaths)
        else:
            self.__country_dict[country_name] = Name_data(date, cases, deaths)

    def __add_to_continent(self, continent_name, date, cases, deaths):
        if continent_name in self.__continent_dict:
            self.__continent_dict[continent_name].add(date, cases, deaths)
        else:
            self.__continent_dict[continent_name] = Name_data(date, cases, deaths)

    def __get_month(self, month):
        return Covid_service.__month_dict[month]

    def __get_date(self, day, month_name):
        return '{0}.{1}.2020'.format(day, self.__get_month(month_name))

    def make_data(self):
        for line in islice(self.__file, 1, None):
            temp_line = line.split()

            if 12 >= len(temp_line) > 10:
                country = temp_line[6]
                continent = temp_line[10]
                deaths = int(temp_line[5])
                cases = int(temp_line[4])
                date = temp_line[0]

                self.__add_to_country(country, date, cases, deaths)
                self.__add_to_continent(continent, date, cases, deaths)

    def get_country(self, country_name):
        return self.__country_dict[country_name]

    def get_continent(self, continent_name):
        return self.__continent_dict[continent_name]

    def get_continent_cases(self, continent_name):
        return self.__continent_dict[continent_name].get_sum_cases()

    def get_continent_deaths(self, continent_name):
        return self.__continent_dict[continent_name].get_sum_deaths()

    def get_country_cases(self, country_name):
        return self.__country_dict[country_name].get_sum_cases()

    def get_country_deaths(self, country_name):
        return self.__country_dict[country_name].get_sum_deaths()

    def get_world_sum(self):
        sum_cases = 0
        sum_deaths = 0

        for country in self.__country_dict.values():
            sum_cases += country.get_sum_cases()
            sum_deaths += country.get_sum_deaths()

        return sum_cases, sum_deaths

    def get_world_month(self, month_name):
        sum_cases = 0
        sum_deaths = 0

        for country in self.__country_dict.values():
            sum_cases += country.get_month_cases(self.__get_month(month_name))
            sum_deaths += country.get_month_deaths(self.__get_month(month_name))

        return sum_cases, sum_deaths

    def get_world_day(self, day, month_name):
        sum_cases = 0
        sum_deaths = 0

        for country in self.__country_dict.values():
            sum_cases += country.get_day_cases(self.__get_date(day, month_name))
            sum_deaths += country.get_day_deaths(self.__get_date(day, month_name))

        return sum_cases, sum_deaths

    def get_country_month_deaths(self, country_name, month_name):
        return self.__country_dict[country_name].get_month_deaths(self.__get_month(month_name))

    def get_country_month_cases(self, country_name, month_name):
        return self.__country_dict[country_name].get_month_cases(self.__get_month(month_name))

    def get_continent_month_deaths(self, continent_name, month_name):
        return self.__continent_dict[continent_name].get_month_deaths(self.__get_month(month_name))

    def get_continent_month_cases(self, continent_name, month_name):
        return self.__continent_dict[continent_name].get_month_cases(self.__get_month(month_name))

    def get_country_day_cases(self, country_name, day, month_name):
        return self.__country_dict[country_name].get_day_cases(self.__get_date(day, month_name))

    def get_country_day_deaths(self, country_name, day, month_name):
        return self.__country_dict[country_name].get_day_deaths(self.__get_date(day, month_name))

    def get_continent_day_cases(self, continent_name, day, month_name):
        return self.__continent_dict[continent_name].get_day_cases(self.__get_date(day, month_name))

    def get_continent_day_deaths(self, continent_name, day, month_name):
        return self.__continent_dict[continent_name].get_day_deaths(self.__get_date(day, month_name))
