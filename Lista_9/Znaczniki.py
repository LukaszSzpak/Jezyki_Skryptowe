import pickle
import re
from LevSim import calc_lev_sim
import numpy as np


class Znaczniki:
    __MAX_DL = 30
    __MIN_DL = 3
    __FILENAME = 'znaczniki.pkl'

    def __init__(self):
        self.__string_list = []
        self.__add_regex = re.compile(r'^((?!_)\w)*_?((?!_)\w)*_?((?!_)\w)*$')

    def add_string(self, string):
        if string in self.__string_list:
            return False

        if self.__add_regex.match(string) is None:
            return False

        if len(string) < Znaczniki.__MIN_DL or len(string) > Znaczniki.__MAX_DL:
            return False

        self.__string_list.append(string)
        return True

    def get_strings(self, reg_string, editing_distnace):
        return_string_list = []

        for string in self.__string_list:
            if calc_lev_sim(reg_string, string) <= editing_distnace:
                return_string_list.append(string)

        return return_string_list

    def get_accepted(self, string_list):
        return_string_list = []

        for get_string in string_list:
            if get_string in self.__string_list:
                return_string_list.append(get_string)

        return  return_string_list

    def get_rejected(self, string_list):
        return np.setdiff1d(string_list, self.get_accepted(string_list))

    def save(self):
        with open(Znaczniki.__FILENAME, 'wb') as output:
            pickle.dump(self.__string_list, output, pickle.HIGHEST_PROTOCOL)

    def open(self):
        with open(Znaczniki.__FILENAME, 'wb') as infile:
            self.__string_list = pickle.load(infile)
