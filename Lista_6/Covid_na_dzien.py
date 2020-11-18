class Covid_na_dzien:
    def __init__(self, day, month, year, cases, deaths):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__cases = int(cases)
        self.__deaths = int(deaths)

    def get_date(self):
        return self.__day + '/' + self.__month + '/' + self.__year + '\t'

    def get_cases(self):
        return self.__cases

    def get_deaths(self):
        return self.__deaths

    def __str__(self):
        return self.__day + '/' + self.__month + '/' + self.__year + '\t' \
               + str(self.__cases) + '\t' \
               + str(self.__deaths)

    @classmethod
    def from_line(cls, line):
        temp_data = line.split()
        if len(temp_data) > 5:
            temp_date = temp_data[0].split('.')
            return cls(temp_date[0], temp_date[1], temp_date[2], temp_data[4], temp_data[5])

    @classmethod
    def from_data(cls, date, cases, deaths):
        temp_date = date.split('.')
        return cls(temp_date[0], temp_date[1], temp_date[2], cases, deaths)


if __name__ == '__main__':
    ob1 = Covid_na_dzien('10', '04', '2019', '67', '2')
    ob2 = Covid_na_dzien.from_data('02.05.2017', '764', '4')
    ob3 = Covid_na_dzien.from_line('04.08.2020	4	8	2020	37	4	Afghanistan	AF	AFG	38041757	Asia	2,97567749')

    print str(ob1)
    print str(ob2)
    print str(ob3)
