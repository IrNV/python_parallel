from multiprocessing import Pool
from math import sin, cos
from time import clock


def doubler(x):
    """
    Иттерационная функция суммирования (sum не используем)
    """
    result = 0
    for ind, val in enumerate(x):
        result += sin(cos(sin(cos(sin(cos(val))))))

    return result


if __name__ == '__main__':
    numbers = [i for i in range(1000000)]
    procs = []

    # Параллельно суммируем списки чисел
    start_time = clock()
    pool = Pool(processes=4)
    print(pool.map(doubler, [numbers for i in range(10)]))
    print(clock() - start_time)

    # Последовательно суммируем списки чисел
    start_time = clock()
    for i in range(1):
        result = 0
        for ind, val in enumerate(numbers):
            result += sin(cos(sin(cos(sin(cos(val))))))
    print(clock() - start_time)
