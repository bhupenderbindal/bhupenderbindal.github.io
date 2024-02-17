## PASTING SUCH A PATTERN WILL CAUSE LOSS OF NEWLINE OPERATOR
##FUCKING HELL WILL READ AS A SINGLE LINE THEN SHITTY SHIT

# do same stuff for rows and columns
# check whether total num is odd or even
# if odd check on n-1)/2 and +1 and check individually
# if at n-1)/2 reject last and if at +1 reject first
# if even then check at n/2
#

import numpy as np


def main():
    part1()
    part2()


def part2():
    hor_patterns, ver_patterns = create_patterns_arr()
    # iterate over rows if row and next match then if the diff of parts = 1 then add to result
    # if row and next row diff = 1 then check the two parts are equal or not
    p = 0
    i = 0
    for pattern in hor_patterns:
        a = hor_sum(pattern)
        if a:
            i += 1
            p += a

        # if nparr_diff_one(pattern[i], pattern[i+1]):

    for pattern in ver_patterns:
        b = ver_sum(pattern)
        if b:
            i += 1
            p += b
    # print(p)
    print(i)
    res = 0

    i = 0
    for pattern in hor_patterns:
        a = hor_sum2(pattern)
        if a:
            i += 1
            res += a

    # if nparr_diff_one(pattern[i], pattern[i+1]):

    for pattern in ver_patterns:
        b = ver_sum2(pattern)
        if b:
            i += 1
            res += b
    print(i)

    print(res)


def hor_sum(pattern):
    for i in range(pattern.shape[0] - 1):
        if np.array_equal(pattern[i], pattern[i + 1]):
            if i >= int(len(pattern) / 2):
                common_len = len(pattern) - 1 - i

                if are_nparr_mirror(
                    pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]
                ):
                    # print(pattern[i + 1 - common_len : i + 1], pattern[i + 1 :])
                    return 100 * (i + 1)
            else:
                common_len = i + 1

                if are_nparr_mirror(
                    pattern[:common_len], pattern[common_len : common_len * 2]
                ):
                    return 100 * (i + 1)


def hor_sum2(pattern):
    for i in range(pattern.shape[0] - 1):
        # if np.array_equal(pattern[i], pattern[i + 1]):
        if i >= int(len(pattern) / 2):
            common_len = len(pattern) - 1 - i
            # print(common_len, (pattern.shape[0] - 1 - i))

            if nparr_diff_one(pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]):
                # print(pattern[i + 1 - common_len : i + 1], pattern[i + 1 :])
                return 100 * (i + 1)
        else:
            common_len = i + 1

            if nparr_diff_one(
                pattern[:common_len], pattern[common_len : common_len * 2]
            ):
                return 100 * (i + 1)
        # if nparr_diff_one(pattern[i], pattern[i + 1]):
        #     pattern[i] = pattern[i + 1]
        #     # print(pattern)
        #     m = hor_sum(pattern)
        #     if m:
        #         # print(m)
        #         return m


def ver_sum2(pattern):
    for i in range(pattern.shape[0] - 1):
        # if np.array_equal(pattern[i], pattern[i + 1]):
        if i >= int(len(pattern) / 2):
            common_len = len(pattern) - 1 - i

            if nparr_diff_one(pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]):
                return i + 1
        else:
            common_len = i + 1

            if nparr_diff_one(
                pattern[:common_len], pattern[common_len : common_len * 2]
            ):
                return i + 1
        # if nparr_diff_one(pattern[i], pattern[i + 1]):
        #     pattern[i] = pattern[i + 1]
        #     m = ver_sum(pattern)
        #     if m:
        #         return m


def ver_sum(pattern):
    for i in range(pattern.shape[0] - 1):
        if np.array_equal(pattern[i], pattern[i + 1]):
            if i >= int(len(pattern) / 2):
                common_len = len(pattern) - 1 - i

                if are_nparr_mirror(
                    pattern[i + 1 - common_len : i + 1], pattern[i + 1 :]
                ):
                    return i + 1
            else:
                common_len = i + 1

                if are_nparr_mirror(
                    pattern[:common_len], pattern[common_len : common_len * 2]
                ):
                    return i + 1


def nparr_diff_one(a: np.ndarray, b: np.ndarray):
    if len(b.shape) == 2:
        b = np.flip(b, 0)
    # else:
    #     print(a, b, np.compare_chararrays(a, b, "!=", True).sum())
    # print(a, c)
    # print(np.compare_chararrays(a, c, "!=", True).sum())
    if np.compare_chararrays(a, b, "!=", True).sum() == 1:
        # print(a, b, np.compare_chararrays(a, b, "!=", True).sum())
        return True
    else:
        return False


def part1():
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

## ideal solution:

# import numpy as np

# def mirrorpos(arr, axis=0, diff=0):
#     m = np.array(arr, dtype=int)
#     if axis == 1:
#         m = m.T
#     for i in range(m.shape[0] - 1):
#         upper_flipped = np.flip(m[: i + 1], axis=0)
#         lower = m[i + 1 :]
#         rows = min(upper_flipped.shape[0], lower.shape[0])
#         if np.count_nonzero(upper_flipped[:rows] - lower[:rows]) == diff:
#             return i + 1
#     return 0

# with open("day13input.txt", "r") as file:
#     data = file.read().split("\n\n")
# for i in range(2):
#     total = 0
#     for puzzle in data:
#         arr = []
#         for line in puzzle.splitlines():
#             arr.append([*line.strip().replace(".", "0").replace("#", "1")])
#         total += 100 * mirrorpos(arr, axis=0, diff=i) + mirrorpos(arr, axis=1, diff=i)
#     print(total)
