import os
import threading


def calculate_squares(numbers):
    for num in numbers:
        square = num * num
        print(
            f"Square of the number {num} is {square} | "
            f"Thread Name {threading.current_thread().name} | "
            f"PID of the process {os.getpid()}"
        )


if __name__ == "__main__":
    numbers = list(range(10**3))
    half = len(numbers) // 2
    first_half = numbers[:half]
    second_half = numbers[half:]

    t1 = threading.Thread(target=calculate_squares, name="t1",
                          args=(first_half,))
    t2 = threading.Thread(target=calculate_squares, name="t2",
                          args=(second_half,))
    t3 = threading.Thread(target=calculate_squares, name="t3",
                          args=(second_half,))

    t1.start()
    t1.join()

    t2.start()
    t3.start()

    t2.join()
    t3.join()
