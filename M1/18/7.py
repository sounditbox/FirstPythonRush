from multiprocessing import Process, Pool
import os
import time
import random


def square(number):
    return number ** 2


if __name__ == "__main__":
    # Creating a random list of integers having size 10^7.
    numbers = [random.randrange(1, 50) for i in range(10 ** 6)]

    start_time = time.time()
    with Pool(4) as p:
        p.map(square, numbers)
    end_time = time.time()  # End time without multiprocessing
    print(
        f"Execution Time Without Multiprocessing: {(end_time - start_time)}")


