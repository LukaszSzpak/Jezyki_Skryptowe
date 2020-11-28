from LevSim import calc_lev_sim

class Przedmioty:
    def __init__(self):
        self.__subject_dict = {}

    def get_subject_code(self, subject_name):
        if not self.__subject_dict:
            return None

        temp_list = []
        act_div = 0
        while not temp_list:
            for code, name in self.__subject_dict.items():
                if calc_lev_sim(name, subject_name) <= act_div:
                    temp_list.append(code)
                act_div += 1

        if len(temp_list) > 1:
            return None
        return temp_list[0]

    def add_subject(self, subject_code, subject_name):
        if subject_code in self.__subject_dict.keys() or subject_name in self.__subject_dict.values():
            return -1

        self.__subject_dict[subject_code] = subject_name
        return len(self.__subject_dict.keys())

    def get_subject(self, subject_code):
        if subject_code in self.__subject_dict.keys():
            return self.__subject_dict[subject_code]
        return None

    def __str__(self):
        return str(self.__subject_dict)
