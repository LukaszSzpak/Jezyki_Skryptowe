from Osoba import Osoba
from datetime import date

PUBLISH_OFFSET = 18


class Pracownik(Osoba):
    def __init__(self, names, surname, my_date):
        Osoba.__init__(self, names=names, surname=surname, my_date=my_date)
        self.__publish_list = []

    def add_publish(self, publish_year, publish_score):
        self.__publish_list.append((publish_year, publish_score))

    def get_score_sum_for_4_years(self):
        score_sum = 0

        for temp_publish in self.__publish_list:
            if date.today().year - temp_publish[0] <= 3:
                score_sum += temp_publish[1]

        return score_sum

    def get_years_without_publish(self):
        years_dict = {}
        return_years_list = []

        for (publish_year, publish_score) in self.__publish_list:
            if publish_year not in years_dict.keys():
                years_dict[publish_year] = 1

        for year in range(self._date.year + PUBLISH_OFFSET, date.today().year+1):
            if year not in years_dict.keys():
                return_years_list.append(year)

        return return_years_list
