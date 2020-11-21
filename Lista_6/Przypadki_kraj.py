from Covid_na_dzien import Covid_na_dzien


class Przypadki_kraj:
    def __init__(self, country_code):
        self.country_code = country_code
        self.__day_list = []
        self.__cases_sum = 0
        self.__deaths_sum = 0
        self.__worst_day = None

    def __str__(self):
        return self.country_code + "\t" \
               + str(len(self.__day_list)) + "\t" \
               + str(self.__cases_sum) + "\t" \
               + str(self.__deaths_sum)

    def __lt__(self, other):
        return self.__cases_sum < other.__cases_sum

    def __gt__(self, other):
        return self.__cases_sum > other.__cases_sum

    def __eq__(self, other):
        return self.__cases_sum == other.__cases_sum

    def __day_not_allready_exist(self, date):
        temp_day = Covid_na_dzien.from_data(date, 0, 0)

        for day in self.__day_list:
            if day.get_date() == temp_day.get_date():
                return False

        return True

    def __check_and_swap_worst_day(self, day):
        if day.get_deaths() > self.__worst_day.get_deaths():
            self.__worst_day = day

    def add_day_line(self, line):
        temp_day = Covid_na_dzien.from_line(line)
        data_from_line = line.split()

        if len(data_from_line) >= 9:
            if data_from_line[8] != self.country_code:
                return False

            for day in self.__day_list:
                if day.get_date() == temp_day.get_date():
                    return False

            self.__day_list.append(temp_day)
            self.__check_and_swap_worst_day(temp_day)
            self.__cases_sum += temp_day.get_cases()
            self.__deaths_sum += temp_day.get_deaths()
            return True
        return False

    def add_day_data(self, date, cases, deaths):
        if self.__day_not_allready_exist(date):
            temp_day = Covid_na_dzien.from_data(date, cases, deaths)
            self.__day_list.append(temp_day)
            self.__check_and_swap_worst_day(temp_day)
            self.__deaths_sum += deaths
            self.__cases_sum += cases

            return True
        return False

    def get_country_code(self):
        return self.country_code

    def get_worst_day(self):
        return (self.__worst_day.get_date(), self.__worst_day.get_deaths()) if self.__worst_day else None

    @classmethod
    def from_line(cls, line):
        data_from_line = line.split()

        if len(data_from_line) >= 9:
            temp_obj = cls(data_from_line[8])
            temp_obj.add_day_line(line)

            return temp_obj

    @classmethod
    def from_data(cls, date, cases, deaths, country_code):
        temp_obj = cls(country_code)
        temp_obj.add_day_data(date, cases, deaths)

        return temp_obj


if __name__ == '__main__':
    ob1 = Przypadki_kraj("PL")
    ob1.add_day_data("23.04.2020", 56, 3, )
    ob1.add_day_data("23.04.2020", 50000, 200)
    ob1.add_day_data("25.04.2020", 100, 10)

    ob2 = Przypadki_kraj.from_line("04.08.2020	4	8	2020	37	4	Afghanistan	AF	AFG	38041757	Asia	2,97567749")
    ob3 = Przypadki_kraj.from_data("01.05.2019", 45, 1, "DE")

    print str(ob1)
    print str(ob2)
    print str(ob3)

    print ob1 == ob2
    print ob1 == ob1
    print ob2 > ob3
    print ob2 < ob3
