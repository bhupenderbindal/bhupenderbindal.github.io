import numpy as np


def main():
    solver_day13(difference=0)
    solver_day13(difference=1)


def solver_day13(difference):
    hor_patterns = create_patterns_arr()

    res = 0
    for pattern in hor_patterns:
        a = hor_sum(pattern, difference=difference)
        res += a * 100
        res += hor_sum(np.transpose(pattern), difference=difference)

    print(res)


def hor_sum(pattern, difference: int):
    for i in range(pattern.shape[0] - 1):
        if i >= int(len(pattern) / 2):
            common_len = len(pattern) - 1 - i

            if nparr_diff(
                pattern[i + 1 - common_len : i + 1], pattern[i + 1 :], difference
            ):
                return i + 1
        else:
            common_len = i + 1

            if nparr_diff(
                pattern[:common_len],
                pattern[common_len : common_len * 2],
                difference,
            ):
                return i + 1
    return 0


def nparr_diff(a: np.ndarray, b: np.ndarray, diff: int):
    if len(b.shape) == 2:
        b = np.flip(b, 0)
    if np.compare_chararrays(a, b, "!=", True).sum() == diff:
        return True
    else:
        return False


def are_nparr_mirror(a, b):
    b = b[::-1]
    if np.array_equal(a, b):
        return True
    else:
        return False


def create_patterns_arr():
    hor_patterns = []
    with open("./input.txt", mode="r") as f:
        a = []
        for line in f.readlines():
            if line == "\n":
                hor_patterns.append(np.array(a))
                a = []
            else:
                # a.append(list(map(map_func, list(line[:-1]))))
                # both works: above with encoded below with chars
                a.append(list(line[:-1]))

        hor_patterns.append(np.array(a))
    return hor_patterns


def map_func(x):
    str_map = {".": 0, "#": 1}
    return str_map[x]


if __name__ == "__main__":
    main()


# TOLEARN
# map a str or list of str to numbers using basic python
# here numpy library was used
# transpose a str in regtangular form
