# Homework

## Закінчити функцію

```python
def get_primes_amount(num: int) -> int:
    result = 0
    for i in num:
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        result += 1

    return result

numbers = [40000, 400, 1000000, 700]

for i in numbers:
    print(i)

# NOTE: Щож. Ця реалізація займає досить багато часу...
#       Було б чудово, якби люди, які передають менші числа отримували результатми швидше ніж ті, хто передають великі значення

# NOTE: Обмеження максимального числа - 1000000

# TODO: Закінчіть цю функцію
# TODO: Застосуйте асинхронне програмування
```

