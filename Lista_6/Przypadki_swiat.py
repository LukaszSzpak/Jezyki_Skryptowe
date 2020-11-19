from itertools import islice
from Przypadki_kraj import Przypadki_kraj


class Przypadki_swiat:
    def __init__(self):
        self.__country_dict = {}

    def __check_code_in_dict(self, country_code):
        return country_code in self.__country_dict

    def add_from_file(self, file_path):
        open_file = open(file_path, "r")

        for line in islice(open_file, 1, None):
            country_code = line.split()[8]

            if self.__check_code_in_dict(country_code):
                self.__country_dict[country_code].add_day_line(line)
            else:
                self.__country_dict[country_code] = Przypadki_kraj.from_line(line)


if __name__ == '__main__':
    ob = Przypadki_swiat()
    ob.add_from_file('Covid19.txt')
