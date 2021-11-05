def isPrimeNumber(n):
    if n < 2:
        return False

    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

primeNumbers = []
notPrimeNumbers = []
for x in range(1, 101):
    if isPrimeNumber(x):
        primeNumbers.append(x)
    else:
        notPrimeNumbers.append(x)
print('Números primos de 1 a 100: ', primeNumbers)
print('\n')
print('Números não primos de 1 a 100: ', notPrimeNumbers)