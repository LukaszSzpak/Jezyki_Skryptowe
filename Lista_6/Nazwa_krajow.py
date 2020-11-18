from LevSim import calc_lev_sim

LEV_LEVEL_NAME = 2


class Nazwa_krajow:
    def __init__(self):
        self.__country_dict = {}

    def add_country(self, country_code, country_name, continent):
        if self.__country_dict.has_key(country_code):
            return False
        else:
            for temp_code, (temp_country, temp_continent) in self.__country_dict.items():
                if calc_lev_sim(country_name, temp_country) <= LEV_LEVEL_NAME:
                    return False

            self.__country_dict[country_code] = (country_name, continent)
            return True

    def add_country_line(self, line):
        line_data = line.split()

        if len(line_data) >= 11:
            return self.add_country(line_data[8], line_data[6], line_data[10])

    def print_list(self):
        print self.__country_dict

    def __str__(self):
        return self.__country_dict


if __name__ == '__main__':
    ob = Nazwa_krajow()
    ob.add_country('PL', 'Poland', 'Europe')
    ob.add_country('PL', 'Pol', 'Eur')
    ob.add_country('PT', 'Pola', 'Euro')
    ob.add_country('DE', 'Germany', 'Europe')
    ob.add_country_line(
        '31.07.2020	31	7	2020	71	0	Afghanistan	AF	AFG	38041757	Asia	3,86943221')

    ob.print_list()
