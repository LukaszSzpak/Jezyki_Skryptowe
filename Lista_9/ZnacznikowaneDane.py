import pickle
from Etykieta import Etykieta


class ZnacznikowaneDane:
    __FILENAME = 'znacznikowaneDane.pkl'

    def __init__(self):
        self.__data_list = []

    def get_list(self):
        return self.__data_list

    def add_object(self, object, label):
        for list_object, list_label in self.__data_list:
            if list_object == object:
                return False

        self.__data_list.append((object, label))
        return True

    def save(self):
        with open(ZnacznikowaneDane.__FILENAME, 'wb') as output:
            pickle.dump(self.__data_list, output, pickle.HIGHEST_PROTOCOL)

    def open(self):
        with open(ZnacznikowaneDane.__FILENAME, 'rb') as infile:
            self.__data_list = pickle.load(infile)

    def __eq__(self, other):
        returned_list = list(
            filter(lambda obj: obj[1] == other, self.__data_list)
        )
        return_object = ZnacznikowaneDane()
        return_object.__data_list = returned_list

        return return_object

    def __ne__(self, other):
        returned_list = list(
            filter(lambda obj: obj[1] != other, self.__data_list)
        )
        return_object = ZnacznikowaneDane()
        return_object.__data_list = returned_list

        return return_object

    def __le__(self, other):
        returned_list = list(
            filter(lambda obj: obj[1] <= other, self.__data_list)
        )
        return_object = ZnacznikowaneDane()
        return_object.__data_list = returned_list

        return return_object

    def __ge__(self, other):
        returned_list = list(
            filter(lambda obj: obj[1] >= other, self.__data_list)
        )
        return_object = ZnacznikowaneDane()
        return_object.__data_list = returned_list

        return return_object
