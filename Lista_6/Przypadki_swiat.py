import operator
from itertools import islice
from Przypadki_kraj import Przypadki_kraj
from Covid_na_dzien import Covid_na_dzien


class Przypadki_swiat:
    def __init__(self):
        self.__country_dict = {}
        self.__continent_deaths_dict = {}
        self.__date_death_dict = {}

    def __check_code_in_dict(self, country_code):
        return country_code in self.__country_dict

    def add_from_file(self, file_path):
        open_file = open(file_path, "r")

        for line in islice(open_file, 1, None):
            temp_line = line.split()

            if 12 >= len(temp_line) > 10:
                country_code = temp_line[8]
                continent = temp_line[10]
                deaths = int(temp_line[5])
                date = temp_line[1] + '/' + temp_line[2] + '/' + temp_line[3]

                if self.__check_code_in_dict(country_code):
                    self.__country_dict[country_code].add_day_line(line)
                else:
                    self.__country_dict[country_code] = Przypadki_kraj.from_line(line)

                if continent in self.__continent_deaths_dict.keys():
                    if deaths > self.__continent_deaths_dict[continent].get_deaths():
                        self.__continent_deaths_dict[continent] = Covid_na_dzien.from_line(line)
                else:
                    self.__continent_deaths_dict[continent] = Covid_na_dzien.from_line(line)

                if date in self.__date_death_dict:
                    self.__date_death_dict[date] += deaths
                else:
                    self.__date_death_dict[date] = deaths

    def get_list_country_worst_day(self):
        temp_list = []

        for country in self.__country_dict.values():
            temp_list.append((country.get_country_code(), country.get_worst_day()))

        return temp_list

    def get_continent_dict(self):
        return self.__continent_deaths_dict

    def get_worst_day(self):
        return max(self.__date_death_dict.iteritems(), key=operator.itemgetter(1))


if __name__ == '__main__':
    ob = Przypadki_swiat()
    ob.add_from_file('Covid19.txt')
