from Day_data import Day_data

class Name_data:
    def __init__(self, data, cases, deaths):
        self.__date_dict = {data: Day_data(cases, deaths)}

    def add(self, date, cases, deaths):
        if date in self.__date_dict.keys():
            self.__date_dict[date].add(cases, deaths)
        else:
            self.__date_dict[date] = Day_data(cases, deaths)

    def get(self):
        return self.__date_dict

    def get_day(self, date):
        return self.__date_dict[date]
