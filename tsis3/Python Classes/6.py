def is_prime (n):
    if n < 2:
        return False

    for i in (2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

numbers = []
for element in input().split():
    numbers.append(int(element))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)