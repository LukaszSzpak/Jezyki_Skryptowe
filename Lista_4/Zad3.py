def make_list_of_primes(startInt, howMany):
    primeList = []
    while len(primeList) != howMany:
        startInt += 1
        flag = True
        for i in range(2, (startInt/2) + 1):
            if startInt % i == 0:
                flag = False
        if flag:
            primeList.append(startInt)

    return ", ".join(str(x) for x in primeList)


if __name__ == '__main__':
    firstNumber = raw_input("Put your number: ")
    secondNumber = raw_input("How many primes ? ")
    if firstNumber.isdigit() and secondNumber.isdigit():
        print (make_list_of_primes(int(firstNumber), int(secondNumber)))
    else:
        print ("Nan")
