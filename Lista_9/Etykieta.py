import pickle

from Znaczniki import Znaczniki


class Etykieta:
    __FILENAME = 'etykieta.pkl'

    def __init__(self, string_list):
        self.__znacznik = Znaczniki()

        for string in string_list:
            self.__znacznik.add_string(string)

    def add_string(self, new_string):
        return self.__znacznik.add_string(new_string)

    def get_all_strings(self):
        return self.__znacznik.get_all()

    def save(self):
        with open(Etykieta.__FILENAME, 'wb') as output:
            pickle.dump(self.__znacznik, output, pickle.HIGHEST_PROTOCOL)

    def open(self):
        with open(Etykieta.__FILENAME, 'rb') as infile:
            self.__znacznik = pickle.load(infile)

    def __add__(self, other):
        temp_etykieta = Etykieta(self.__znacznik.get_all())

        for string in other.get_all_strings():
            temp_etykieta.add_string(string)

        return temp_etykieta

    def __mul__(self, other):
        list_str = other.get_all_strings()
        return Etykieta(list(set(list_str).intersection(self.get_all_strings())))

    def __sub__(self, other):
        return_list = [x for x in other.get_all_strings() if x not in self.get_all_strings()]
        return Etykieta(return_list)

    def __eq__(self, other):
        return set(self.get_all_strings()) == set(other.get_all_strings())

    def __ge__(self, other):
        return all(x in self.get_all_strings() for x in other.get_all_strings())

    def __le__(self, other):
        return all(x in other.get_all_strings() for x in self.get_all_strings())

    def __ne__(self, other):
        return list(set(other.get_all_strings()).intersection(self.get_all_strings())) == []
