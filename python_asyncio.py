import asyncio
from math import sin, cos
from time import clock


def send_func(x):
    """
    Функция расчетов, какие занимают длительное время, например, тригонометрические функции
    от нескольких тригонометрических функций.
    """
    return sin(cos(sin(cos(sin(cos(x))))))

async def func(x):
    return send_func(x)

a = clock()
print(a)
loop = asyncio.get_event_loop()
# 100 функций func
tasks = [loop.create_task(func(i)) for i in range(100)]
# print(tasks)
wait_tasks = asyncio.wait(tasks)
result = loop.run_until_complete(wait_tasks)
# print(result)
print(clock() - a)


