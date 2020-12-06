class Day_data:
    def __init__(self, cases, deaths):
        self.__cases = cases
        self.__deaths = deaths

    def add(self, cases, deaths):
        self.__cases += cases
        self.__deaths += deaths

    def get_tuple(self):
        return self.__cases, self.__deaths

    def get_cases(self):
        return self.__cases

    def get_deaths(self):
        return self.__deaths
