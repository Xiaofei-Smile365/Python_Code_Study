# -*- coding: UTF-8 -*-

"""

@Project Name: Python_Code_Study
@File Name:    Guess_Number_AI

@User:         smile
@Author:       Smile
@Email:        Xiaofei.Smile365@Gmail.com

@Date Time:    2020/12/8 下午 02:25
@IDE:          PyCharm

"""

import time
import datetime


def main():
    start_time = time.time()
    print("--- Here is main code! ---", "\n")
    print("The game for AI-Guess-Number in (0, 999) Start now!")
    print("Please input a number in (0, 999) to guess for AI:")
    your_number = input()
    print("You input a number and it is [%s]" % your_number, "\n")

    print("I am a AI and start guess your number now!")

    my_list = []
    ts = 0
    for i in range(0, 1000):
        my_list.append(int(i))

    def binary_search(arr, l, r, x, times):
        if r >= l:
            mid = int((l + r)/2)
            times = times + 1
            print(mid)

            if int(arr[mid]) == x:
                return mid, times
            elif int(arr[mid]) > x:
                return binary_search(arr, l, mid - 1, int(your_number), times)
            else:
                return binary_search(arr, mid + 1, r, int(your_number), times)
        else:
            return -1, times

    result, ts = binary_search(my_list, 0, len(my_list) - 1, int(your_number), ts)

    if result != -1:
        print("I Guess the number is %s and The times is %s\n" % (my_list[result], ts))
    else:
        print("I am Sorry, can't guess it!")

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
