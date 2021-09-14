#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the circumference of a circle
#    with the radius provided by user

import constants


def main():

    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference is {0}mm.".format(circumference))


if __name__ == "__main__":
    main()
