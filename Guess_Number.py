# -*- coding: UTF-8 -*-

"""

@Project Name: Python_Code_Study
@File Name:    Guess_Number

@User:         smile
@Author:       Smile
@Email:        Xiaofei.Smile365@Gmail.com

@Date Time:    2020/12/8 下午 01:20
@IDE:          PyCharm

"""

import time
import datetime
import random


def main():
    start_time = time.time()
    print("--- Here is main code! ---", "\n")
    print("The game for Guess-Number in (0, 999) Start now!")
    random_number = random.randint(0, 999)
    print("The random number has been generated and it is [***]!", "\n")
    while True:
        print("Please input your number:")
        your_number = input()
        if str(your_number).isdigit() is True:
            print("You input a number and it is %s" % your_number)
            print("Check it...")
            if int(your_number) > random_number:
                print("Your number is Bigger, Please try again!", "\n")
            elif int(your_number) < random_number:
                print("Your number is Smaller, Please try again!", "\n")
            elif int(your_number) == random_number:
                print("Your number is Right, The Game is Over", "\n")
                break
        else:
            print("Please input a number!", "\n")

    end_time = time.time()
    start_end = end_time - start_time

    return start_end


if __name__ == '__main__':
    print("* [Start] for the Program in %s" % datetime.datetime.now(), "\n")
    consuming = main()
    print("* [End] for the Program in %s" % datetime.datetime.now(), "\n")
    print("[Program time consuming] is %s s" % consuming)
    time.sleep(3)

    pass
