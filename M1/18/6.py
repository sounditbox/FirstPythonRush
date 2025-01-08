from multiprocessing import Process
import os
import time
import random


def calculate_squares(numbers):
    for num in numbers:
        square = num * num


if __name__ == "__main__":
    # Creating a random list of integers having size 10^7.
    numbers = [random.randrange(1, 50) for i in range(10 ** 7)]
    half = len(numbers) // 2
    first_half = numbers[:half]
    second_half = numbers[half:]

    # ----------------- Creating Single Process Environment ------------------------#

    start_time = time.time()  # Start time without multiprocessing

    p1 = Process(
        target=calculate_squares, args=(numbers,)
    )  # Single process P1 is executing all list
    p1.start()
    p1.join()

    end_time = time.time()  # End time without multiprocessing
    print(
        f"Execution Time Without Multiprocessing: {(end_time - start_time) * 10 ** 3}ms")

    # ----------------- Creating Multi Process Environment ------------------------#

    start_time = time.time()  # Start time with multiprocessing

    p2 = Process(target=calculate_squares, args=(first_half,))
    p3 = Process(target=calculate_squares, args=(second_half,))

    p2.start()
    p3.start()

    p2.join()
    p3.join()

    end_time = time.time()  # End time with multiprocessing
    print(
        f"Execution Time With Multiprocessing: {(end_time - start_time) * 10 ** 3}ms")

    # ----------------- Creating Multi Process Environment ------------------------#

    start_time = time.time()  # Start time with multiprocessing

    p2 = Process(target=calculate_squares, args=(first_half,))
    p3 = Process(target=calculate_squares, args=(second_half,))
    p4 = Process(target=calculate_squares, args=(first_half,))

    p2.start()
    p3.start()
    p4.start()

    p2.join()
    p3.join()
    p4.join()

    end_time = time.time()  # End time with multiprocessing
    print(
        f"Execution Time With Multiprocessing(3): {(end_time - start_time) * 10 ** 3}ms")
