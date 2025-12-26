import re
from sys import set_int_max_str_digits


def main():
    test_cases: list[list[tuple[float, float]]] = list()
    while(True):
        command = int(input(int))
        if command == 0:
            break
        else:
            test_case_n:list[tuple[float, float]] = list()
            for _ in range(command):
                count: int = 0
                temp = list()
                for x in input().split():
                    if count == 2:
                        break
                    else:
                        temp.append(float(x))
                        count += 1
                temp = tuple(temp)
            test_cases.append(test_case_n)
            for _ in range(len(test_cases)):
                result_n = solve(sorted(test_case_n, key = get_x),
                                 sorted(test_case_n, key = get_y)
                                )
                for i in range(len(result_n)):
                    if i < len(result_n) - 1:
                        print(result_n[i], end=" ")
                    else:
                        print(result_n[i])

def get_x(tup: tuple[float, float]) -> float:
    return tup[0]

def get_y(tup: tuple[float, float]) -> float:
    return tup[1]



def pivot(sample_x: list[tuple[float, float]],
        sample_y: list[tuple[float, float]]) \
        -> tuple[list[tuple[float, float]], \
        list[tuple[float, float]], list[tuple[float, float]], \
    list[tuple[float, float]]] | None:
    """Return px_l, py_l, px_r, py_r and hori_line_pos_x"""
    if len(sample_x) >= 2:
        hori_line_pos_x = len(sample_x) // 2
        px_l: list[tuple[float, float]] = sample_x[hori_line_pos_x:]
        px_r: list[tuple[float, float]] = sample_x[:hori_line_pos_x]

        py_l: list[tuple[float, float]] = delete_points_by_y(sample_y, hori_line_pos_x, True)
        py_r: list[tuple[float, float]] = delete_points_by_y(sample_y, hori_line_pos_x, False)
        py_r: list[tuple[float, float]] = sorted(px_r, key = get_y)

        return (px_l, py_l, px_r, py_r)
    else:
        return None



def delete_points_by_x(sample_x: list[tuple[float, float]], line: float, \
                       d: float) -> list[tuple[float, float]]:
    li = sample_x.copy()
    for pt in li:
        if (line - d) < pt[0] < (line + d):
            li.remove(pt)
    return li


def delete_points_by_y(sample_y: list[tuple[float, float]], mid: float, \
                       is_lower_x: bool) -> list[tuple[float, float]]:
    li = sample_y.copy()
    if is_lower_x:
        for pt in li:
            if pt[1] > mid:
                li.remove(pt)
    else:
        for pt in li:
            if pt[1] <= mid:
                li.remove(pt)
    return li



def solve(sample_x: list[tuple[float, float]],
          sample_y: list[tuple[float, float]],
          hori_line_pos_x: float | None = None) \
        -> list[tuple[float, float]]:
    """Return list of tuple which is """
    if not hori_line_pos_x:
        return [
            (sample_x[0][0], sample_x[0][1]),
            (sample_x[1][0], sample_x[1][1])
        ]
    px_l, py_l, px_r, py_r = pivot(sample_x, sample_y)
    d1 = solve(px_l, py_l)
    d2 = solve(px_r, py_r)
    d = min(d1, d2)


    px_l = delete_points_by_x(px_l, hori_line_pos_x, d)
    py_l = delete_points_by_x(py_l, hori_line_pos_x, d)
    px_r = delete_points_by_x(px_r, hori_line_pos_x, d)
    py_r = delete_points_by_x(py_r, hori_line_pos_x, d)

    return ((sample_x[1][0] - sample_x[0][0]) ** 2) + ((sample_x[1][1] - sample_x[0][1]) ** 2))



if __name__ == "__main__":
    main()
