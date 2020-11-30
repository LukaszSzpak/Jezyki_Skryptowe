from Osoba import Osoba
from Pracownik import Pracownik
from Przedmioty import Przedmioty
from Student import Student


def get_data_list():
    list = []

    p1 = Pracownik('Adam', 'Nowak', '1974-03-11')
    p1.add_publication('2020', 6)
    p1.add_publication('2020', 8)
    list.append(p1)

    p2 = Pracownik('Elan', 'Datem', '1976-05-13')
    p2.add_publication('2018', 10)
    p2.add_publication('2017', 43)
    p2.add_publication('2007', 190)
    list.append(p2)

    p3 = Pracownik('Tom', 'Kish', '1994-11-09')
    list.append(p3)

    stud1 = Student('Lukas', 'Spak', '1999-09-07')
    stud1.add_mark('WF', '5.0')
    stud1.add_mark('ANG', '4.5')
    list.append(stud1)
    stud2 = Student('Kluba', 'Nowa', '1997-11-07')
    stud2.add_mark('BIO', '2.0')
    stud2.add_mark('ANG', '4.5')
    list.append(stud2)
    stud3 = Student('Jan', 'Smit', '1998-11-18')
    stud3.add_mark('BIO', '5.0')
    stud3.add_mark('MT', '3.5')
    list.append(stud3)
    stud4 = Student('Pablo', 'Ciech', '2000-05-02')
    stud4.add_mark('ANG', '5.5')
    stud4.add_mark('MT', '2.5')
    list.append(stud4)
    stud5 = Student('Agata', 'Nowak', '2001-06-24')
    stud5.add_mark('BIO', '4.5')
    stud5.add_mark('WF', '5.5')
    list.append(stud5)

    return list


def get_subject():
    sub1 = Przedmioty()
    sub1.add_subject('MT', 'Matematyka')
    sub1.add_subject('WF', 'Wuef')
    sub1.add_subject('WF', 'Waf')
    sub1.add_subject('ANG', 'Angielski')
    sub1.add_subject('PL', 'Polski')
    sub1.add_subject('BIO', 'Biologia')

    return sub1


def max_pkt_count(emplo_list):
    max = 0
    for emplo in emplo_list:
        if emplo.get_score_sum_for_4_years() > max:
            max = emplo.get_score_sum_for_4_years()

    result_list = []
    for emplo in emplo_list:
        if emplo.get_score_sum_for_4_years() == max:
            result_list.append(emplo)

    return result_list


if __name__ == '__main__':
    my_list = get_data_list()
    subjects = get_subject()
    emplo_list_40_50 = []
    emplo_list = []
    stud_list = []

    for person in my_list:
        if isinstance(person, Pracownik):
            if 40 <= person.get_age_in_years() <= 50:
                emplo_list_40_50.append(person)
            emplo_list.append(person)

        if isinstance(person, Student):
            stud_list.append(person)

    print('Max pkt: ')
    for emplo in max_pkt_count(emplo_list_40_50):
        print(str(emplo))

    print('\nStudenci w kolejności alfabetycznej: ')
    stud_list.sort(key=lambda student: student.get_surname_and_name())
    for student in stud_list:
        print(str(student))

    print('\nPracownicy w kolejnosci alfabetycznej:')
    emplo_list.sort(key=lambda employee: employee.get_surname_and_name())
    for employee in emplo_list:
        print(str(employee))

    print('\nStudencie wedlug ocen:')
    stud_list.sort(key=lambda student: student.get_average())
    for student in stud_list:
        print('Ocena: ' + str(student.get_average()) + ' |Dane: ' + str(student))

    for student in stud_list:
        if student.get_surname() == 'Ciech':
            print(str(student.get_all_marks()) + ' Srednia: ' + str(student.get_average()))
