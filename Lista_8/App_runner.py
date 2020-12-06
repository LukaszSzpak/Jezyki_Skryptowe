from Covid_serv import  Covid_service

if __name__ == '__main__':
    covid = Covid_service()
    covid.make_data()

    print(covid.get_continent('Asia'))
