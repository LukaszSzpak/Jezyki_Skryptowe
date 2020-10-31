def isPrime(myInt):
    while True:
        myInt += 1
        flag = True
        for i in range(2, (myInt/2) + 1):
            if myInt % i == 0:
                flag = False
        if flag:
            return myInt


if __name__ == '__main__':
    line = raw_input("Put your number: ")
    if line.isdigit():
        print (isPrime(int(line)))
    else:
        print ("Nan")
