def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res <= 1:
            print("Не простое и не составное")
        elif res == 2:
            print("Простое")
        elif res % 2 == 0:
            print("Составное")
        else:
            prime = True
            for i in range(3, int(res ** 0.5) + 1, 2):  # Проверяем только нечетные числа
                if res % i == 0:
                    prime = False
                    break
            if prime:
                print("Простое")
            else:
                print("Составное")
        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
