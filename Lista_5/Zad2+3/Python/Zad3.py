import time

MYFILENAME = '../Covid19.txt'


if __name__ == '__main__':
    my_file = open(MYFILENAME, "r")

    sum_ = 0
    country = input('Write your country: ')
    start_time = time.time()

    for line in my_file:
        word_list = line.split()

        if len(word_list) >= 7 and word_list[6] == country:
            sum_ += int(word_list[4]) if word_list[4].isdigit() else 0

    print('Total cases: %d' % sum_)
    print('Exec time: %f' % (time.time() - start_time))
