list = [4, 5, 48, 2, 6, 8, 1, 0, 67, 34, 7, 9]


def print_SMA(number_list, step, value, last_value):
    if len(number_list) > 0:
        print (str(value))
        print_SMA(number_list[1::], step, value + float(float(number_list[0] - last_value) / step), number_list[0])


if __name__ == '__main__':
    number_list = list[1::]
    step = list[0]

    if len(number_list) <= step:
        print ("None")
    else:
        sum = 0
        for i in range(0, step):
            sum += number_list[i]
        print_SMA(number_list[step::], step, float(sum/float(step)), number_list[step-1])