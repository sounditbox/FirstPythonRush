import os
from multiprocessing import Process, Pool


def calculate_squares(numbers):
    for i, num in enumerate(numbers):
        square = num * num
        print(f"{i}. PID: {os.getpid()}")


if __name__ == "__main__":
    numbers = list(range(10**5))
    half = len(numbers) // 2
    first_half = numbers[:half]
    second_half = numbers[half:]

    p1 = Process(target=calculate_squares, args=(first_half,))
    p2 = Process(target=calculate_squares, args=(second_half,))

    p2.start()
    p1.start()

    p1.join()
    p2.join()
