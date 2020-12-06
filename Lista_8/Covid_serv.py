from itertools import islice

FILE_PATH = "Covid19.txt"


class Covid:
    def __init__(self):
        self.__file = open(FILE_PATH, 'r')

    def get_country_date_dict(self, country_name):
        country_dict = {}

        for line in islice(self.__file, 1, None):
            temp_line = line.split()

            if 12 >= len(temp_line) > 10:
                country = temp_line[6]
                deaths = int(temp_line[5])
                cases = int(temp_line[4])
                date = temp_line[1] + '-' + temp_line[2] + '-' + temp_line[3]

                if country == country_name:
                    if date not in country_dict.keys():
                        country_dict[date] = (cases, deaths)
                    else:
                        country_dict[date][0] += cases
                        country_dict[date][1] += deaths

        return country_dict
    # dict date: (cases, deaths)

    def get_continent_date_dict(self, continent_name):
        continent_dict = {}

        for line in islice(self.__file, 1, None):
            temp_line = line.split()

            if 12 >= len(temp_line) > 10:
                continent = temp_line[10]
                deaths = int(temp_line[5])
                cases = int(temp_line[4])
                date = temp_line[1] + '-' + temp_line[2] + '-' + temp_line[3]

                if continent == continent_name:
                    if date not in continent_dict.keys():
                        continent_dict[date] = (cases, deaths)
                    else:
                        continent_dict[date][0] += cases
                        continent_dict[date][1] += deaths

        return continent_dict
    # dict date: (cases, deaths)

    def get_world_date(self):
        date_dict = {}

        for line in islice(self.__file, 1, None):
            temp_line = line.split()

            if 12 >= len(temp_line) > 10:
                deaths = int(temp_line[5])
                cases = int(temp_line[4])
                date = temp_line[1] + '-' + temp_line[2] + '-' + temp_line[3]

                if date not in date_dict.keys():
                    date_dict[date] = (cases, deaths)
                else:
                    date_dict[date][0] += cases
                    date_dict[date][1] += deaths

        return date_dict
    # dict date: (cases, deaths)
