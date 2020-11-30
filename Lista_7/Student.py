from Osoba import Osoba


class Student(Osoba):
    def __init__(self, names, surname, my_date):
        Osoba.__init__(self, names=names, surname=surname, my_date=my_date)
        self.__mark_list = []

    def add_mark(self, subject_code, subject_mark):
        if 2 > float(subject_mark) > 5.5:
            return False

        for code, mark in self.__mark_list:
            if code == subject_code and mark != '2.0':
                return False
        self.__mark_list.append((subject_code, subject_mark))
        return True

    def get_average(self):
        sum = 0
        for code, mark in self.__mark_list:
            sum += float(mark)

        return sum/len(self.__mark_list)

    def __str__(self):
        return super().__str__() + ' Number of marks: ' + str(len(self.__mark_list))

    def get_all_marks(self):
        return self.__mark_list
