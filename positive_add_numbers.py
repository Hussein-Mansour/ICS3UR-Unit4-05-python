#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Mon/May17/2021
# This program uses a continue statement


def main():
    # this function add positive numbers
    counter = 0
    sum_of_numbers = 0

    # input
    positive = input("How many numbers you are going to add: ")

    # process  & output
    try:
        positive_int = int(positive)

        while (counter < positive_int):
            counter = counter + 1
            add = input("Enter a number to add: ")
            add_int = int(add)

            if (add_int < 0):
                continue

            sum_of_numbers = sum_of_numbers + add_int

        print(
            "Sum of just the positive numbers is = {}".format(sum_of_numbers)
            )

    except Exception:
        print("\nInvalid input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
