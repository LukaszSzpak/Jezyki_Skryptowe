list = [1, 'l', 6, "lala", 9, 0, 9]


def calc_variance(calc_list, count, ave):
    var = 0
    for i in calc_list:
        var += float((i - ave) ** 2)

    return var / count


if __name__ == '__main__':
    new_list = [i for i in list if isinstance(i, int)]
    sum = sum(new_list)
    count = len(new_list)
    average = float(sum / count)
    min = min(new_list)
    max = max(new_list)
    variance = calc_variance(new_list, count, average)

    print ("Liczba liczb: " + str(count))
    print ("Srednia: " + str(average))
    print ("Wariancja: " + str(variance))
    print ("Min: " + str(min))
    print ("Max: " + str(max))