# -*- coding: UTF-8 -*-

"""

@Project Name: Python_Code_Study
@File Name:    Fizz_Buzz

@User:         smile
@Author:       Smile
@Email:        Xiaofei.Smile365@Gmail.com

@Date Time:    2020/12/8 下午 02:02
@IDE:          PyCharm

"""

import time
import datetime


def main():
    start_time = time.time()
    print("--- Here is main code! ---", "\n")
    print("0")
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    end_time = time.time()
    start_end = end_time - start_time

    return start_end


if __name__ == '__main__':
    print("* [Start] for the Program in %s" % datetime.datetime.now(), "\n")
    consuming = main()
    print("* [End] for the Program in %s" % datetime.datetime.now(), "\n")
    print("[Program time consuming] is %s s" % consuming)

    pass
