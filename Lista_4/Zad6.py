from decimal import Decimal
import sys
#n = (nie wyszlo)

pi_ref = Decimal(3.14159265358979323846)


def calc_pi(n_num):
    pi_sum = Decimal(1.00)

    for n in range(1, n_num):
        n_2 = Decimal(n * 2.00)
        pi_sum *= n_2 / Decimal(n_2 - Decimal(1.00))
        pi_sum *= n_2 / Decimal(n_2 + Decimal(1.00))

    return pi_sum * Decimal(2.00)


def check_pi():
    pi_sum = Decimal(1.00)
    n = 1

    while Decimal(pi_sum * Decimal(2.00)) < pi_ref:
        n_2 = Decimal(n * 2.00)
        pi_sum *= n_2 / Decimal(n_2 - Decimal(1.00))
        pi_sum *= n_2 / Decimal(n_2 + Decimal(1.00))
        n += 1

    print ("n=" + str(n))


if __name__ == '__main__':
    n_number = raw_input("Write n: ")

    if n_number.isdigit():
        print ("Pi: " + str(calc_pi(int(n_number))))

        if len(sys.argv) > 1:
            if sys.argv[1] == "/p":
                check_pi()

    else:
        print ("None")