from datetime import date
from dateutil.relativedelta import relativedelta


class Osoba:
    idCounter = 0

    def __init__(self, names, surname, my_date):
        if type(names) is list and len(names) > 3:
            raise ValueError

        self._name_list = (names if type(names) is list else [names])
        self._surname = surname
        self._date = date.fromisoformat(my_date)
        self._id = Osoba.idCounter

        Osoba.idCounter += 1

    def __str__(self):
        mystr = str(self._id) + ', ' + self._surname + ', '
        for name in self._name_list:
            mystr += name + ', '

        mystr += str(self._date)

        return mystr

    def get_age_in_years(self):
        return relativedelta(date.today(), self._date).years

    def get_surname_and_name(self):
        mystr = self._surname
        for name in self._name_list:
            mystr += name + ', '
        return mystr
