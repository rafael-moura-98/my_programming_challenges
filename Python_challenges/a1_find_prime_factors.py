def prime_factors(number: int) -> list:
    divisor = 2
    keeper = 0
    numbers = list()

    while(number > 1):

        if (number % divisor == 0):
            keeper = number / divisor
            numbers.append(divisor)
            number = keeper
        else:
            divisor += 1

    return numbers

fatores_primos = prime_factors(800)

print(fatores_primos)