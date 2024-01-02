def find_primes(end):
    primes = set(range(0, end))
    k = 2

    while k < end:
        for number in set(primes) - set([k]):
            if (number % k) == 0:
                primes.remove(number)

        k += 1

    return primes


def sorted_list(myList):
    myList = list(myList)
    myList.sort()
    return myList


def calculate_expression(string):
    return string
