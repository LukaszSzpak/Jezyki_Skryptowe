from App_controller import App_controller


def tests():
    covid = App_controller()

    print(covid.deaths_world())
    print(covid.deaths_world(date_month='lipiec'))
    print(covid.deaths_world(date_month='czerwiec', date_day='05'), '\n\n')

    print(covid.cases_world())
    print(covid.cases_world(date_month='lipiec'))
    print(covid.cases_world(date_month='czerwiec', date_day='05'), '\n\n')

    print(covid.deaths_country(country_name='Poland'))
    print(covid.deaths_country(country_name='Poland', date_month='lipiec'))
    print(covid.deaths_country(country_name='Poland', date_month='lipiec', date_day='15'), '\n\n')

    print(covid.cases_country(country_name='Poland'))
    print(covid.cases_country(country_name='Poland', date_month='lipiec'))
    print(covid.cases_country(country_name='Poland', date_month='lipiec', date_day='15'))

    print(covid.get_max_cases(10))


if __name__ == '__main__':
    tests()
