from LevSim import calc_lev_sim

class Przedmioty:
    def __init__(self):
        self.subject_dict = {}

    def get_subject_code(self, subject_name):
        if not self.subject_dict:
            return None

        temp_list = []
        act_div = 0
        while not temp_list:
            for code, name in self.subject_dict.items():
                if calc_lev_sim(name, subject_name) <= act_div:
                    temp_list.append(code)
                act_div += 1

        if len(temp_list) > 1:
            return None
        return temp_list[0]

    def add_subject(self, subject_code, subject_name):
        if subject_code in self.subject_dict.keys() or subject_name in self.subject_dict.values():
            return -1

        self.subject_dict[subject_code] = subject_name
        return len(self.subject_dict.keys())

    def get_subject(self, subject_code):
        if subject_code in self.subject_dict.keys():
            return self.subject_dict[subject_code]
        return None

    def __str__(self):
        return str(self.subject_dict)
