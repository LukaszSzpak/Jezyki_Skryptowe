from Osoba import Osoba
from datetime import date

PUBLICATION_OFFSET = 18


class Pracownik(Osoba):
    def __init__(self, names, surname, my_date):
        Osoba.__init__(self, names=names, surname=surname, my_date=my_date)
        self.__publication_list = []

    def add_publication(self, publication_year, publication_score):
        self.__publication_list.append((int(publication_year), int(publication_score)))

    def get_score_sum_for_4_years(self):
        score_sum = 0

        for temp_publication in self.__publication_list:
            if date.today().year - temp_publication[0] <= 3:
                score_sum += temp_publication[1]

        return score_sum

    def get_years_without_publication(self):
        years_dict = {}
        return_years_list = []

        for (publication_year, publication_score) in self.__publication_list:
            if publication_year not in years_dict.keys():
                years_dict[publication_year] = 1

        for year in range(self._date.year + PUBLICATION_OFFSET, date.today().year+1):
            if year not in years_dict.keys():
                return_years_list.append(year)

        return return_years_list

    def __str__(self):
        return super(Pracownik, self).__str__() + ', Number of publications: ' + str(len(self.__publication_list))
