import asyncio


async def sort_val(val):
    await asyncio.sleep(val)
    print(val, end=" ", flush=True)


async def sleep_sort(values):
    tasks = [sort_val(val) for val in values]
    await asyncio.gather(*tasks)

import random

# lst = [6, 1, 999]
lst = [random.randint(0, 2) for _ in range(1000)]
print("Avant le tri: ", lst)
print("Après le tri: ", end="")
asyncio.run(sleep_sort(lst))
