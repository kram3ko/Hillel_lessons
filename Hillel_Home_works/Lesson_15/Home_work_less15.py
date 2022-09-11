import asyncio
from random import randint

numbers = [randint(1, 10000) for i in range(10)]
print(numbers)


async def get_primes_amount(num: int) -> int:
    result = 0

    for i in range(2, num + 1):
        counter = 0
        for j in range(1, i+1):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        if counter == 2:
            result += 1

        await asyncio.sleep(0)

    print(result)
    return result


async def manager():
    """"giving tasks to gather"""
    # digits = [get_primes_amount(num) for num in numbers]
    await asyncio.gather(*[get_primes_amount(num) for num in numbers])


if __name__ == "__main__":
    asyncio.run(manager())
