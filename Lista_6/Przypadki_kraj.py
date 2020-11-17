from Covid_na_dzien import Covid_na_dzien

class Przypadki_kraj:
    def __init__(self, country_code):
        self.country_code = country_code
        self.__day_list = []
        self.__cases_sum = 0
        self.__deaths_sum = 0

    def __str__(self):
        return self.country_code + "\t" \
               + str(len(self.__day_list)) + "\t" \
               + str(self.__cases_sum) + "\t" \
               + str(self.__deaths_sum)

    def add_day(self, line):
        temp_day = Covid_na_dzien.from_line(line)
        data_from_line = line.split()

        if len(data_from_line) >= 9:
            if data_from_line[8] != self.country_code:
                return False

            for day in self.__day_list:
                if day.get_date() == temp_day.get_date():
                    return False

            self.__day_list.append(temp_day)
            return True
        return False
