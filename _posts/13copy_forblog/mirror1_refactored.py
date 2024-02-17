# do same stuff for rows and columns
# check whether total num is odd or even
# if odd check on n-1)/2 and +1 and check individually
# if at n-1)/2 reject last and if at +1 reject first
# if even then check at n/2
#

import numpy as np


def main():
    hor_patterns, ver_patterns = create_patterns_arr()
    # print(is_even(patt_list[1]))
    res = 0

    for pattern in hor_patterns:

        for i in range(pattern.shape[0] - 1):
            if np.array_equal(pattern[i], pattern[i + 1]):
                if i >= int(len(pattern) / 2):
                    common_len = len(pattern) - 1 - i

                    if are_nparr_mirror(
                        pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]
                    ):
                        res += 100 * (i + 1)
                else:
                    common_len = i + 1

                    if are_nparr_mirror(
                        pattern[:common_len], pattern[common_len : common_len * 2]
                    ):
                        res += 100 * (i + 1)

    for pattern in ver_patterns:
        for i in range(pattern.shape[0] - 1):
            if np.array_equal(pattern[i], pattern[i + 1]):
                if i >= int(len(pattern) / 2):
                    common_len = len(pattern) - 1 - i

                    if are_nparr_mirror(
                        pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]
                    ):
                        res += i + 1
                else:
                    common_len = i + 1

                    if are_nparr_mirror(
                        pattern[:common_len], pattern[common_len : common_len * 2]
                    ):
                        res += i + 1

    print(res)


def are_nparr_mirror(a, b):
    b = b[::-1]
    if np.array_equal(a, b):
        return True
    else:
        return False


def create_patterns_arr():
    hor_patterns = []
    ver_patterns = []
    with open("./input.txt", mode="r") as f:
        a = []
        for line in f.readlines():
            if line == "\n":
                hor_patterns.append(np.array(a))
                ver_patterns.append(np.transpose(np.array(a)))
                a = []
            else:
                # a.append(list(map(map_func, list(line[:-1]))))
                # both works: above with encoded below with chars
                a.append(list(line[:-1]))

        hor_patterns.append(np.array(a))
        ver_patterns.append(np.transpose(np.array(a)))
    return hor_patterns, ver_patterns


def map_func(x):
    str_map = {".": 0, "#": 1}
    return str_map[x]


if __name__ == "__main__":
    main()


# TOLEARN
# map a str or list of str to numbers using basic python
# here numpy library was used
# transpose a str in regtangular form
