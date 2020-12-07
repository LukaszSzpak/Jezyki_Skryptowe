from App_controller import App_controller


class _RangeError(Exception): pass


class Console:
    def __init__(self):
        self.__location = None
        self.__deaths_cases = None
        self.__date_month = None
        self.__date_day = None
        self.__range_day = None
        self.__app = App_controller()

    @staticmethod
    def get_string(message, name="string", default=None,
                   minimum_length=0, maximum_length=80,
                   force_lower=False):
        message += ": " if default is None else " [{0}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line:
                    if default is not None:
                        return default
                    if minimum_length == 0:
                        return ""
                    else:
                        raise ValueError("{0} may not be empty".format(
                            name))
                if not (minimum_length <= len(line) <= maximum_length):
                    raise ValueError("{0} must have at least {1} and "
                                     "at most {2} characters".format(name, minimum_length, maximum_length))
                return line if not force_lower else line.lower()
            except ValueError as err:
                print("ERROR", err)

    @staticmethod
    def get_integer(message, name="integer", default=None, minimum=None,
                    maximum=None, allow_zero=True):
        message += ": " if default is None else " [{0}]: ".format(default)
        while True:
            try:
                line = input(message)
                if not line and default is not None:
                    return default
                x = int(line)
                if x == 0:
                    if allow_zero:
                        return x
                    else:
                        raise _RangeError("{0} may not be 0".format(name))
                if ((minimum is not None and minimum > x) or
                        (maximum is not None and maximum < x)):
                    raise _RangeError("{0} must be between {1} and {2} "
                                      "inclusive{3}".format(name, minimum, maximum,
                                                            (" (or 0)" if allow_zero else "")))
                return x
            except _RangeError as err:
                print("ERROR", err)
            except ValueError as err:
                print("ERROR {0} must be an integer".format(name))

    def start_app(self):

        while True:
            command = Console.get_string('Wybierz opcje - dzien / zakres lub exit aby wyjść')

            if command == 'dzien':
                self.__deaths_cases = Console.get_string('Wybierz rodzaj - zgony / zachorowania',
                                                         default=self.__deaths_cases)
                self.__location = Console.get_string('Podaj lokalizacje - np. swiat, Asia, Poland',
                                                     default=self.__location)
                self.__date_month = Console.get_string('Podaj miesiac <opjonalne>',
                                                       default=self.__date_month)

                self.__date_month = self.__date_month if not self.__date_month == '' else None
                if self.__date_month is not None:
                    self.__date_day = Console.get_string('Podaj dzień miesiąca <opjonalnie>',
                                                         default=self.__date_day)
                    if self.__date_day == '':
                        self.__date_day = None
                    elif len(self.__date_day) == 1:
                        self.__date_day = '0{0}'.format(self.__date_day)
                else:
                    self.__date_day = None

                if self.__deaths_cases == 'zgony':
                    print(self.__app.check_location_and_get_deaths(location=self.__location,
                                                                   date_month=self.__date_month,
                                                                   date_day=self.__date_day))
                elif self.__deaths_cases == 'zachorowania':
                    print(self.__app.check_location_and_get_cases(location=self.__location,
                                                                  date_month=self.__date_month,
                                                                  date_day=self.__date_day))
                else:
                    print('Błędny wybór rodzaju !')

            elif command == 'zakres':
                self.__deaths_cases = Console.get_string('Wybierz rodzaj - zgony / zachorowania',
                                                         default=self.__deaths_cases)
                self.__range_day = Console.get_integer("Podaj ilość dni - (1-30)", minimum=1, maximum=30,
                                                       allow_zero=False, default=self.__range_day)

                if self.__deaths_cases == 'zgony':
                    print(self.__app.get_max_deaths(self.__range_day))
                elif self.__deaths_cases == 'zachorowania':
                    print(self.__app.get_max_cases(self.__range_day))
                else:
                    print('Błędny wybór rodzaju !')
            elif command == 'exit':
                break
            else:
                print('Bledny wybór !')


if __name__ == '__main__':
    console = Console()
    console.start_app()
