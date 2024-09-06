def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res == 0 or res == 1:
            print("Не простое и не составное")
        elif (res % 2 == 0 and res % res == 0) or (res % 3 == 0 and res % res == 0):
            print("Составное")
        else:
            print("Простое")
        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(1)
print(result)
