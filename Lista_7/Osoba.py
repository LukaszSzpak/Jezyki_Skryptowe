from datetime import date
from dateutil.relativedelta import relativedelta


class Osoba:
    idCounter = 0

    def __init__(self, names, surname, my_date, ):
        if type(names) is list and len(names) > 3:
            raise ValueError

        self.__name_list = (names if type(names) is list else [names])
        self.__surname = surname
        self.__date = date.fromisoformat(my_date)
        self.__id = Osoba.idCounter

        Osoba.idCounter += 1

    def __str__(self):
        mystr = str(self.__id) + ', '
        for name in self.__name_list:
            mystr += name + ', '

        mystr += self.__surname + ', ' + str(self.__date)

        return mystr

    def getAgeInYears(self):
        return relativedelta(date.today(), self.__date).years
