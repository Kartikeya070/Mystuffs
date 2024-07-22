#making a function of factorial
def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number=input("enter a number")
print(factorial_iterative(number))