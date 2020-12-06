# coding=utf-8
from itertools import islice

from Covid.LevSim import calc_lev_sim

LEV_LEVEL_NAME = 2


class Nazwa_krajow:
    def __init__(self):
        self.__country_dict = {}

    def add_country(self, country_code, country_name, continent):
        if country_code in self.__country_dict.keys():
            return False
        else:
            for temp_code, (temp_country, temp_continent) in self.__country_dict.items():
                if calc_lev_sim(country_name, temp_country) < LEV_LEVEL_NAME:
                    return False

            self.__country_dict[country_code] = (country_name, continent)
            return True

    def add_country_line(self, line):
        line_data = line.split()

        if len(line_data) is 12:
            return self.add_country(line_data[8], line_data[6], line_data[10])

    def add_from_file(self, file_path):
        open_file = open(file_path, "r")

        for line in islice(open_file, 1, None):
            self.add_country_line(line)

    def get_country_name(self, code):
        try:
            return self.__country_dict[code][0]
        except KeyError:
            return 'Brak'

    def get_code_for_country(self, country):
        temp_country_dict = {}
        act_level = 0

        while not len(temp_country_dict):
            for temp_code, (temp_country, temp_continent) in self.__country_dict.items():
                if calc_lev_sim(country, temp_country) <= act_level:
                    temp_country_dict[temp_country] = (str(act_level), temp_code)

            act_level += 1

        if len(temp_country_dict) == 1:
            return str(temp_country_dict.keys()[0]) + ' ' + str(temp_country_dict.values()[0][1]) \
                   + ' ' + str(temp_country_dict.values()[0][0])
        else:
            return 'Niejednoznaczność nazwy: %d kandydatów' % len(temp_country_dict)

    def print_list(self):
        print(self.__country_dict)

    def __str__(self):
        return self.__country_dict
