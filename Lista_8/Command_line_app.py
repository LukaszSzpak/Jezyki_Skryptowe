from App_controller import App_controller
import sys


def print_help():
    print('Wywołanie aplikacji: \n'
          'python3 Command_line_app.py <zgony/zachorowania> <lokalizacja> <data_miesiac> <data_dzien>\n'
          'zgony/zachorowania - pole wymagane\n'
          'lokalizacja - pole wymagane swiat / "kontynent" / "kraj" \n'
          'data_miesiac - pole opcjonalne np. lipiec\n'
          'data_dzien - pole opcjonalne np. 06\n'
          'pole dzien nie może wysępować bez miesiąca !'
          'lub\n'
          'python3 Command_line_app.py zakres <zgony/zachorowania> <ilosc_dni>\n'
          'ilosc_dni - pole wymagane od 1 do 30/n'
          'zgony/zachorowania - pole wymagane\n'
          )


if __name__ == '__main__':
    app = App_controller()

    arg_list = sys.argv[1:]
    if not arg_list:
        print('Brak argumentów ! użyj "help"')

    elif arg_list[0] == 'help':
        print_help()

    elif len(arg_list) == 2:
        if arg_list[0] == 'zgony':
            print(app.check_location_and_get_deaths(location=arg_list[1]))
        elif arg_list[0] == 'zachorowania':
            print(app.check_location_and_get_cases(location=arg_list[1]))
        else:
            print('Błędny wybór !')

    elif len(arg_list) == 3:
        if arg_list[0] == 'zakres':
            if not 1 <= int(arg_list[2]) <= 30:
                print('Zakres dni poza skalą !')
            elif arg_list[1] == 'zgony':
                print(app.get_max_deaths(int(arg_list[2])))
            elif arg_list[1] == 'zachorowania':
                print(app.get_max_cases(int(arg_list[2])))
            else:
                print('Błędny wybór !')
        else:
            if arg_list[0] == 'zgony':
                print(app.check_location_and_get_deaths(location=arg_list[1], date_month=arg_list[2]))
            elif arg_list[0] == 'zachorowania':
                print(app.check_location_and_get_cases(location=arg_list[1], date_month=arg_list[2]))
            else:
                print('Błędny wybór !')

    elif len(arg_list) == 4:
        if arg_list[0] == 'zgony':
            print(app.check_location_and_get_deaths(location=arg_list[1], date_month=arg_list[2], date_day=arg_list[3]))
        elif arg_list[0] == 'zachorowania':
            print(app.check_location_and_get_cases(location=arg_list[1], date_month=arg_list[2], date_day=arg_list[3]))
        else:
            print('Błędny wybór !')
