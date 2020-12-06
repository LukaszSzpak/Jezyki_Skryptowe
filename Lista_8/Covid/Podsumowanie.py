# coding=utf-8
from Covid.Przypadki_swiat import Przypadki_swiat
from Covid.Nazwa_krajow import Nazwa_krajow


if __name__ == '__main__':
    worst_country = ('', 0)
    worst_continent = ('', 0)

    world = Przypadki_swiat()
    world.add_from_file('Covid19.txt')

    codes = Nazwa_krajow()
    codes.add_from_file('Covid19.txt')

    print('Najgorszy dzień kontynentu: ')
    for continent_name, continent_day in world.get_continent_dict().items():
        print (continent_name + ': ' + continent_day.get_date())

        if continent_day.get_deaths() > worst_continent[1]:
            worst_continent = (continent_name, continent_day.get_deaths())

    print('\nNajgorszy dzień kraju:')
    for country in world.get_list_country_worst_day():
        if country:
            print (codes.get_country_name(country[0]) + ': ' + country[1][0])

        if country[1][1] > worst_country[1]:
            worst_country = (codes.get_country_name(country[0]), country[1][1])

    print('\nNajgorszy kontynent: ' + worst_continent[0])
    print('Najgorszy kraj: ' + worst_country[0])
    print('Nojgorszy dzień: ' + world.get_worst_day()[0])
