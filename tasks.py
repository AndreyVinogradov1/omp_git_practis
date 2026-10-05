# Задачи пары: раунд 2 — fizzbuzz, раунд 3 — is_prime.

# Вместо ... впишите своё имя, вместо raise NotImplementedError — решение.
# Проверить, что файл запускается без ошибок: python3 tasks.py



def fizzbuzz(n):
    """Вернуть "FizzBuzz", если n делится на 3 и на 5, "Fizz" — только на 3,
    "Buzz" — только на 5, иначе само число строкой."""
    # Реализовал(а): Зуев Михаил
    
    if n%15 == 0:
        return FizzBuzz
    if n%3==0:
        return Fizz
    if n%5==0:
        return Buzz
    else:
        return n

def is_prime(n):
    """Вернуть True, если n — простое число (больше 1 и делится только на 1 и на себя)."""
    # Реализовал(а): Зуев Михаил

    return n>1 and all(n%d!=0 for d in range(1, int(n**0.5)+1))
