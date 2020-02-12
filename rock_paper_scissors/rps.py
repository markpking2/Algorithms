#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps_array = [['rock'], ['paper'], ['scissors']]
    if n == 0:
        return [[]]

    def rps_helper(arr):
        if(len(arr[0]) == n):
            return arr
        else:
            new_arr = []
            for i in range(len(arr)):
                new_arr.append(arr[i] + rps_array[0])
                new_arr.append(arr[i] + rps_array[1])
                new_arr.append(arr[i] + rps_array[2])

            return(rps_helper(new_arr))
    return rps_helper(rps_array)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
