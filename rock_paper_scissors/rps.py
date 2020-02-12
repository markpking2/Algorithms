#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    def rps_helper(arr, iter):
        if(iter == n):
            return arr
        else:
            new_arr = []
            for i in range(len(arr)):
                new_arr.append(arr[i] + ['rock'])
                new_arr.append(arr[i] + ['paper'])
                new_arr.append(arr[i] + ['scissors'])

            return(rps_helper(new_arr, iter + 1))
    return rps_helper([['rock'], ['paper'], ['scissors']], 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
