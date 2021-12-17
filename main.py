import operator
import time
from collections import Counter, deque

import numpy as np
import matplotlib.pyplot as plt


def run():
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    # task_8()
    # task_9()
    # task_10()
    # task_11()
    # task_12()
    # task_13()
    # task_14()
    # task_15()
    # task_16()
    # task_17()
    # task_18()
    # task_19()
    # task_20()
    # task_21()
    # task_22()
    # task_23()
    # task_24()
    # task_25()
    # task_26()
    # task_27()
    # task_28()
    # task_29()
    # task_30()
    # task_31()
    # task_32()
    task_33()
    task_34()
    return


def task_1():
    s = open("data/data_task_1", "r")
    rows = s.readlines()
    s.close()
    rows = [float(row.rstrip()) for row in rows]
    length = len(rows)
    increased_count = 0
    for i in range(1, length):
        if rows[i] > rows[i - 1]:
            increased_count += 1
    print("INCREASED COUNT : {0}".format(increased_count))
    return


def task_2():
    s = open("data/data_task_1", "r")
    rows = s.readlines()
    s.close()
    rows = [float(row.rstrip()) for row in rows]
    rows_length, size = len(rows), 3
    windows = np.array([rows[i:i + size] for i in range(0, rows_length, 1) if i <= rows_length - size])
    windows_length = len(windows)
    increased_count = 0
    for i in range(1, windows_length):
        if windows[i].sum() > windows[i - 1].sum():
            increased_count += 1
    print("INCREASED COUNT : {0}".format(increased_count))
    return


def task_3():
    s = open("data/data_task_3", "r")
    rows = s.readlines()
    s.close()

    def transform(row):
        direction, value = row.rstrip().split(" ")
        return (direction[0], float(value))

    rows = [transform(row) for row in rows]
    horizontal, depth = 0, 0
    for v, u in rows:
        if v == 'f':
            horizontal += u
        if v == 'd':
            depth += u
        if v == 'u':
            depth -= u
    print("HORIZONTAL = {0} DEPTH = {1} AREA = {2}".format(horizontal, depth, horizontal * depth))
    return


def task_4():
    s = open("data/data_task_3", "r")
    rows = s.readlines()
    s.close()

    def transform(row):
        direction, value = row.rstrip().split(" ")
        return (direction[0], float(value))

    rows = [transform(row) for row in rows]
    horizontal, depth, aim = 0, 0, 0
    for v, u in rows:
        if v == 'f':
            horizontal += u
            depth += u * aim
        if v == 'd':
            aim += u
        if v == 'u':
            aim -= u
    print("HORIZONTAL = {0} DEPTH = {1} AREA = {2}".format(horizontal, depth, horizontal * depth))
    return


def task_5():
    s = open("data/data_task_5", "r")
    rows = s.readlines()
    s.close()

    def transform(row):
        bits = row.rstrip()
        return list(bits)

    rows = np.array([transform(row) for row in rows])
    bit_width = len(rows[0])
    most_common_bits, least_common_bits = [], []
    for i in range(bit_width):
        lane = rows[:, i]
        most_common = Counter(lane)
        most_common_bit = most_common.most_common(2)[0][0]
        least_common_bit = most_common.most_common(2)[1][0]
        most_common_bits.append(most_common_bit)
        least_common_bits.append(least_common_bit)
    most_common_bits, least_common_bits = ''.join(most_common_bits), ''.join(least_common_bits)
    gamma, epsilon = int(most_common_bits, 2), int(least_common_bits, 2)
    print("GAMMA = {0} EPSILON = {1} : POWER = {2}".format(gamma, epsilon, gamma * epsilon))
    return


def task_6():
    s = open("data/data_task_5", "r")
    rows = s.readlines()
    s.close()

    def transform(row):
        bits = row.rstrip()
        return list(bits)

    rows = np.array([transform(row) for row in rows])
    bit_width = len(rows[0])

    rows_iter = rows.copy()
    for i in range(bit_width):
        lane = rows_iter[:, i]
        most_common = Counter(lane)
        most_common_bit = most_common.most_common(2)[0]
        least_common_bit = most_common.most_common(2)[-1]
        if most_common_bit[0] != least_common_bit[0] and most_common_bit[1] == least_common_bit[1]:
            most_common_bit = '1'
        else:
            most_common_bit = most_common_bit[0]
        most_common_values = rows_iter[lane == most_common_bit]
        rows_iter = most_common_values
    if len(rows_iter) > 1:
        print("ERROR")
    most_common_bits = rows_iter[0]

    rows_iter = rows.copy()
    for i in range(bit_width):
        lane = rows_iter[:, i]
        least_common = Counter(lane)
        most_common_bit = least_common.most_common(2)[0]
        least_common_bit = least_common.most_common(2)[-1]
        if most_common_bit[0] != least_common_bit[0] and most_common_bit[1] == least_common_bit[1]:
            least_common_bit = '0'
        else:
            least_common_bit = least_common_bit[0]
        least_common_values = rows_iter[lane == least_common_bit]
        rows_iter = least_common_values
    if len(rows_iter) > 1:
        print("ERROR")
    least_common_bits = rows_iter[0]

    most_common_bits, least_common_bits = ''.join(most_common_bits), ''.join(least_common_bits)
    ogr, co2sr = int(most_common_bits, 2), int(least_common_bits, 2)
    print("oxygen generator rating = {0} CO2 scrubber rating = {1} : life support rating = {2}".format(ogr, co2sr, ogr * co2sr))
    return


def task_7():
    s = open("data/data_task_7", "r")
    rows = s.readlines()
    s.close()

    def transform_row(row):
        output = list(map(int, row.rstrip().split()))
        return output

    def transform_grid(grid):
        output = list(map(transform_row, grid))
        output = np.array(output)
        return output

    numbers = list(map(int, rows[0].split(",")))
    grids = np.array(rows[1:]).reshape((-1, 6))[:, 1:]
    grids = list(map(transform_grid, grids))
    grids_count = len(grids)
    grids_won = set()

    for x in numbers:
        for grid_idx, grid in enumerate(grids):
            matches = np.where(grid == x)
            grid[matches] = -1
            rows_sum, columns_sum = grid.sum(axis=0), grid.sum(axis=1)
            if len(np.where(rows_sum == -5)[0]) != 0 or len(np.where(columns_sum == -5)[0]) != 0:
                non_marked_numbers = grid[np.where(grid != -1)]
                non_marked_sum = non_marked_numbers.sum()
                print("BOARD {0} : non_marked_sum={1} with number={2} has score={3}".format(grid_idx + 1, non_marked_sum, x, non_marked_sum * x))
                return

    return


def task_8():
    s = open("data/data_task_7", "r")
    rows = s.readlines()
    s.close()

    def transform_row(row):
        output = list(map(int, row.rstrip().split()))
        return output

    def transform_grid(grid):
        output = list(map(transform_row, grid))
        output = np.array(output)
        return output

    numbers = list(map(int, rows[0].split(",")))
    grids = np.array(rows[1:]).reshape((-1, 6))[:, 1:]
    grids = list(map(transform_grid, grids))
    grids_count = len(grids)
    grids_won = set()

    for x in numbers:
        for grid_idx, grid in enumerate(grids):
            matches = np.where(grid == x)
            grid[matches] = -1
            rows_sum, columns_sum = grid.sum(axis=0), grid.sum(axis=1)
            if len(np.where(rows_sum == -5)[0]) != 0 or len(np.where(columns_sum == -5)[0]) != 0:
                non_marked_numbers = grid[np.where(grid != -1)]
                non_marked_sum = non_marked_numbers.sum()
                grids_won.add(grid_idx)
                if len(grids_won) == grids_count:
                    print("BOARD {0} : non_marked_sum={1} with number={2} has score={3}".format(grid_idx + 1, non_marked_sum, x, non_marked_sum * x))
                    return

    return


def task_9():
    s = open("data/data_task_9", "r")
    rows = s.readlines()
    s.close()

    ##
    def transform(row):
        points = row.rstrip().split(" -> ")
        points = [point.split(",") for point in points]
        points = [list(map(int, point)) for point in points]
        points = np.array(points)
        return points

    lines = [transform(row) for row in rows]
    lines = np.array([line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]])

    dimension = np.max(lines) + 1
    chart = np.zeros((dimension, dimension))

    for line in lines:
        (x1, y1), (x2, y2) = line[0], line[1]
        (x1, y1), (x2, y2) = (min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))
        chart[y1:y2 + 1, x1:x2 + 1] += 1

    overlapping_count = len(np.where(chart >= 2)[0])
    print("Overlapping is {0}".format(overlapping_count))
    return


def task_10():
    s = open("data/data_task_9", "r")
    rows = s.readlines()
    s.close()

    ##
    def transform(row):
        points = row.rstrip().split(" -> ")
        points = [point.split(",") for point in points]
        points = [list(map(int, point)) for point in points]
        points = np.array(points)
        return points

    lines = [transform(row) for row in rows]
    accepted_lines = []

    for line in lines:
        c1, c2 = line[0], line[1]
        diff_c1c2 = np.abs(c1 - c2)
        c1xc2 = c1.dot(c2)
        c1_norm, c2_norm = np.linalg.norm(c1), np.linalg.norm(c2)
        c1c2_cos = c1xc2 / (c1_norm * c2_norm)
        cos_rad = np.arccos(c1c2_cos)
        cos_deg = np.rad2deg(cos_rad)
        ##
        horizontal_or_vertical = c1[0] == c2[0] or c1[1] == c2[1]
        diagonal = diff_c1c2[0] == diff_c1c2[1]
        if horizontal_or_vertical:
            accepted_lines.append((line, '1'))
        if diagonal:
            accepted_lines.append((line, '2'))

    dimension = np.max(lines) + 1
    chart = np.zeros((dimension, dimension))

    for line, v in accepted_lines:
        c1, c2 = line[0], line[1]
        du = (c2 - c1)
        u = (du / (np.abs(du) + 1e-37)).astype(np.int32)
        i = 0
        while True:
            xy = c1 + i * u
            chart[xy[1], xy[0]] += 1
            i += 1
            if (xy == c2).all():
                break

    chart = np.int32(chart)
    overlapping_count = len(np.where(chart >= 2)[0])
    print("Overlapping is {0}".format(overlapping_count))

    # for row in chart:
    #     for c in row:
    #         print("{0}".format(c if c > 0 else "."), end ="")
    #     print("")
    return


def task_11():
    s = open("data/data_task_11", "r")
    rows = s.readline()
    s.close()
    ##
    fishes = list(map(int, rows.split(",")))
    simulation_length = 80

    grid = np.zeros(9)
    for fish in fishes:
        grid[fish] += 1

    for j in range(simulation_length):
        x = grid[0]

        for i in np.arange(1, 9):
            grid[i - 1] = grid[i]
        grid[8] = 0

        grid[6] += x
        grid[8] += x

    print("LANTERNFISH = {0} @ {1}".format(simulation_length, grid.sum()))
    return


def task_12():
    s = open("data/data_task_11", "r")
    rows = s.readline()
    s.close()
    ##
    fishes = list(map(int, rows.split(",")))
    simulation_length = 256

    grid = np.zeros(9)
    for fish in fishes:
        grid[fish] += 1

    for j in range(simulation_length):
        x = grid[0]

        for i in np.arange(1, 9):
            grid[i - 1] = grid[i]
        grid[8] = 0

        grid[6] += x
        grid[8] += x

    print("LANTERNFISH = {0} @ {1}".format(simulation_length, grid.sum()))
    return


def task_13():
    s = open("data/data_task_13", "r")
    data = s.readline()
    s.close()
    ##
    xs = np.array(list(map(int, data.rstrip().split(","))))
    max_xs = xs.max()
    costs = np.zeros(max_xs)
    for i in np.arange(max_xs):
        for x in xs:
            dist = np.abs(x - i)
            costs[i] += dist

    print("MIN_COST = {0}".format(costs.min()))
    return


def task_14():
    s = open("data/data_task_13", "r")
    data = s.readline()
    s.close()
    ##
    xs = np.array(list(map(int, data.rstrip().split(","))))
    max_xs = xs.max()
    costs = np.zeros(max_xs)
    for i in np.arange(max_xs):
        for x in xs:
            dist = np.abs(x - i)
            costs[i] += np.arange(1, dist + 1).sum()

    print("MIN_COST = {0}".format(costs.min()))
    return


def task_15():
    s = open("data/data_task_15", "r")
    rows = s.readlines()
    s.close()

    unique_digits = [["c", "f"], ["b", "c", "d", "f"], ["a", "c", "f"], ["a", "b", "c", "d", "e", "f", "g"]]
    all_digits = [
        ["a", "b", "c", "e", "f", "g"],
        ["c", "f"],
        ["a", "c", "d", "e", "g"],
        ["a", "c", "d", "f", "g"],
        ["b", "c", "d", "f"],

        ["a", "b", "d", "f", "g"],
        ["a", "b", "d", "e", "f", "g"],
        ["a", "c", "f"],
        ["a", "b", "c", "d", "e", "f", "g"],
        ["a", "b", "c", "d", "f", "g"]]

    ##
    def transform(row):
        left, right = row.rstrip().split(" | ")
        left, right = left.split(" "), right.split(" ")
        return left, right

    lines = [transform(row) for row in rows]
    count_1478 = 0

    for _, right in lines:
        for digit in right:
            for unique_digit in unique_digits:
                if len(digit) == len(unique_digit):
                    print("{} : {}".format(digit, unique_digit))
                    count_1478 += 1

    print("count_1478 = {0}".format(count_1478))
    return


def task_16():
    s = open("data/data_task_15", "r")
    rows = s.readlines()
    s.close()

    all_digits = [
        "cagedb",
        "ab",
        "gcdfa",
        "fbcad",
        "eafb",
        "cdfbe",
        "cdfgeb",
        "dab",
        "acedgfb",
        "cefabd"]

    ##
    def transform(row):
        left, right = row.rstrip().split(" | ")
        left, right = left.split(" "), right.split(" ")
        return left, right

    lines = [transform(row) for row in rows]
    count_1478 = 0

    idx_to_digit = [8, 5, 2, 3, 7, 9, 6, 4, 0, 1]

    def build_dict(left):
        k2d, d2k = {}, {}
        for digit in left:
            if len(digit) == 2:
                k2d[digit] = 1
                d2k[1] = digit
            if len(digit) == 3:
                k2d[digit] = 7
                d2k[7] = digit
            if len(digit) == 4:
                k2d[digit] = 4
                d2k[4] = digit
            if len(digit) == 7:
                k2d[digit] = 8
                d2k[8] = digit
        for digit in left:
            if len(digit) == 5 and set(d2k[7]).issubset(set(digit)) and digit not in k2d:
                k2d[digit] = 3
                d2k[3] = digit
        for digit in left:
            if len(digit) == 6 and set(d2k[7]).issubset(set(digit)) and set(d2k[3]).issubset(set(digit)) and digit not in k2d:
                k2d[digit] = 9
                d2k[9] = digit
        for digit in left:
            if len(digit) == 6 and set(d2k[7]).issubset(set(digit)) and digit not in k2d:
                k2d[digit] = 0
                d2k[0] = digit
        for digit in left:
            if len(digit) == 6 and digit not in k2d:
                k2d[digit] = 6
                d2k[6] = digit
        for digit in left:
            if len(digit) == 5 and len(set(d2k[6]).intersection(set(digit))) == 5 and digit not in k2d:
                k2d[digit] = 5
                d2k[5] = digit
        for digit in left:
            if len(digit) == 5 and digit not in k2d:
                k2d[digit] = 2
                d2k[2] = digit
        return k2d, d2k

    sum = 0

    for left, right in lines:
        k2d, d2k = build_dict(left)
        number = ""
        for digit in right:
            for key in k2d.keys():
                if set(digit) == set(key):
                    number += str(k2d[key])
        number = int(number)
        sum += number
    print("sum = {0}".format(sum))
    return


def task_17():
    s = open("data/data_task_17", "r")
    rows = s.readlines()
    s.close()

    #
    def transform(row):
        cave = list(map(int, list(row.rstrip())))
        return cave

    caves = np.array([transform(row) for row in rows])
    h, w = caves.shape
    highest = caves.max()
    padding = np.ones((h + 2, w + 2)) * (highest + 1)
    padding[1:h + 1, 1:w + 1] = caves

    def found(v, x_i, y_i):
        if padding[x_i - 1, y_i] > v and padding[x_i + 1, y_i] > v and padding[x_i, y_i - 1] > v and padding[x_i, y_i + 1] > v:
            return True
        return False

    #
    levels = 0
    for x_i in np.arange(1, h + 1):
        for y_i in np.arange(1, w + 1):
            v = padding[x_i, y_i]
            match = found(v, x_i, y_i)
            if match:
                levels += v + 1

    print("LEVELS = {0}".format(levels))
    return


def task_18():
    s = open("data/data_task_17", "r")
    rows = s.readlines()
    s.close()

    #
    def transform(row):
        cave = list(map(int, list(row.rstrip())))
        return cave

    caves = np.array([transform(row) for row in rows])
    h, w = caves.shape
    highest = caves.max()
    padding = np.ones((h + 2, w + 2)) * 9
    padding[1:h + 1, 1:w + 1] = caves
    states = np.zeros((h + 2, w + 2))

    def found(v, x_i, y_i):
        if states[x_i, y_i] == 1 or v == 9:
            states[x_i, y_i] = 1
            return 0

        states[x_i, y_i] = 1

        basin_size = 1

        if padding[x_i - 1, y_i] < 9:
            basin_size += found(padding[x_i - 1, y_i], x_i - 1, y_i)
        if padding[x_i + 1, y_i] < 9:
            basin_size += found(padding[x_i + 1, y_i], x_i + 1, y_i)
        if padding[x_i, y_i - 1] < 9:
            basin_size += found(padding[x_i, y_i - 1], x_i, y_i - 1)
        if padding[x_i, y_i + 1] < 9:
            basin_size += found(padding[x_i, y_i + 1], x_i, y_i + 1)
        return basin_size

    #
    basins = []
    for x_i in np.arange(1, h + 1):
        for y_i in np.arange(1, w + 1):
            v = padding[x_i, y_i]
            basin_size = found(v, x_i, y_i)
            if basin_size > 0:
                basins.append(basin_size)

    top_3 = sorted(basins)[-3:]
    print("TOP 3 = {0} : {1}".format(top_3, np.prod(top_3)))
    return


def task_19():
    s = open("data/data_task_19", "r")
    rows = s.readlines()
    s.close()

    #
    def transform(row):
        return row.rstrip()

    rows = [transform(row) for row in rows]
    #
    begins, closes, stats = ["(", "[", "{", "<"], [")", "]", "}", ">"], [3, 57, 1197, 25137]
    b2i, c2i = {}, {}
    for idx, begin in enumerate(begins):
        b2i[begin] = stats[idx]
    for idx, close in enumerate(closes):
        c2i[close] = stats[idx]
    #
    syntax_errors = []
    for y, row in enumerate(rows):
        queue = []
        for x, char in enumerate(row):
            e = None
            if char in b2i:
                e = (x, char, 'o', b2i[char])
            if char in c2i:
                e = (x, char, 'c', c2i[char])
            if len(queue) > 0:
                q, previous, mode1, i = queue[-1]
                q, current, mode2, j = e
                if i != j and mode1 != mode2:
                    syntax_errors.append((y, current, j))
                    break
                if i == j and mode1 != mode2:
                    queue.pop(-1)
                    continue
            queue.append(e)
    #
    syntax_error_score = [se[2] for se in syntax_errors]
    syntax_error_score = sum(syntax_error_score)
    print("SYNTAX_ERROR_SCORE = {0}".format(syntax_error_score))
    return


def task_20():
    s = open("data/data_task_19", "r")
    rows = s.readlines()
    s.close()

    #
    def transform(row):
        return row.rstrip()

    rows = [transform(row) for row in rows]
    #
    begins, closes, stats = ["(", "[", "{", "<"], [")", "]", "}", ">"], [1, 2, 3, 4]
    b2i, c2i = {}, {}
    for idx, begin in enumerate(begins):
        b2i[begin] = stats[idx]
    for idx, close in enumerate(closes):
        c2i[close] = stats[idx]
    #
    incomplete = []
    for y, row in enumerate(rows):
        syntax_errors = []
        queue = []
        for x, char in enumerate(row):
            e = None
            if char in b2i:
                e = (x, char, 'o', b2i[char])
            if char in c2i:
                e = (x, char, 'c', c2i[char])
            if len(queue) > 0:
                q, previous, mode1, i = queue[-1]
                q, current, mode2, j = e
                if i != j and mode1 != mode2:
                    syntax_errors.append((y, current, j))
                    break
                if i == j and mode1 != mode2:
                    queue.pop(-1)
                    continue
            queue.append(e)
        if len(queue) > 0 and len(syntax_errors) == 0:
            incomplete.append((y, queue))

    scores = []
    for y, queue in incomplete:
        completetion_string = []
        for (x, char, mode, i) in queue:
            completetion_string.append(char)
        completetion_string.reverse()
        score = 0
        for idx, char in enumerate(completetion_string):
            score = (score * 5) + b2i[char]
        print("score = {0}".format(score))
        scores.append(score)
    middle_score = sorted(scores)[int(len(scores) / 2)]
    print("MIDDLE_SCORE = {0}".format(middle_score))
    #
    return


def task_21():
    s = open("data/data_task_21", "r")
    rows = s.readlines()
    s.close()

    def transform(row):
        row = np.array(list(map(int, list(row.rstrip()))))
        return row

    energy = np.array([transform(row) for row in rows])
    w, h = energy.shape
    steps, flashes = 100, 0

    dirs = [
        (- 1, - 1),
        (+ 0, - 1),
        (+ 1, - 1),
        (+ 1, + 0),
        (+ 1, + 1),
        (+ 0, + 1),
        (- 1, + 1),
        (- 1, + 0),
    ]

    def process(stats, x, y):
        if energy[x + 0, y + 0] > 9:
            energy[x + 0, y + 0] = 0
            stats[x, y] = 0

            local_flashes = 1
            for x_o, y_o in dirs:
                x_c, y_c = x + x_o, y + y_o
                if x_c < 0 or y_c < 0 or x_c >= energy.shape[0] or y_c >= energy.shape[1]:
                    continue
                energy[x_c, y_c] = energy[x_c, y_c] + 1 * stats[x_c, y_c]
                if energy[x_c, y_c] > 9:
                    local_flashes += process(stats, x_c, y_c)
            return local_flashes

        return 0

    for i in np.arange(steps):
        stats = np.ones(energy.shape)
        energy = energy + 1
        for x in np.arange(w):
            for y in np.arange(h):
                flashes += process(stats, x, y)

    print("FLASHES = {0}".format(flashes))
    return


def task_22():
    s = open("data/data_task_21", "r")
    rows = s.readlines()
    s.close()

    def transform(row):
        row = np.array(list(map(int, list(row.rstrip()))))
        return row

    energy = np.array([transform(row) for row in rows])
    w, h = energy.shape
    steps, flashes = 1000, 0

    dirs = [
        (- 1, - 1),
        (+ 0, - 1),
        (+ 1, - 1),
        (+ 1, + 0),
        (+ 1, + 1),
        (+ 0, + 1),
        (- 1, + 1),
        (- 1, + 0),
    ]

    def process(stats, x, y):
        if energy[x + 0, y + 0] > 9:
            energy[x + 0, y + 0] = 0
            stats[x, y] = 0

            local_flashes = 1
            for x_o, y_o in dirs:
                x_c, y_c = x + x_o, y + y_o
                if x_c < 0 or y_c < 0 or x_c >= energy.shape[0] or y_c >= energy.shape[1]:
                    continue
                energy[x_c, y_c] = energy[x_c, y_c] + 1 * stats[x_c, y_c]
                if energy[x_c, y_c] > 9:
                    local_flashes += process(stats, x_c, y_c)
            return local_flashes

        return 0

    step = 0
    for i in np.arange(steps):
        stats = np.ones(energy.shape)
        energy = energy + 1
        for x in np.arange(w):
            for y in np.arange(h):
                process(stats, x, y)
        if energy.sum() == 0:
            step = i
            break

    print("STEP = {0}".format(step + 1))
    return


def task_23():
    s = open("data/data_task_23", "r")
    rows = s.readlines()
    s.close()

    start, cave_to_stats, transitions, end = set(), {}, set(), set()

    for row in rows:
        x, y = row.rstrip().split("-")
        x_big_cave, y_big_cave = x.isupper(), y.isupper()
        cave_to_stats[x] = x_big_cave
        cave_to_stats[y] = y_big_cave
        transitions.add((x, y))

    paths = []

    def build_path(path):
        v = path[-1]
        if v == "end":
            print("{0}".format(path))
            paths.append(path)
            return

        counts = dict(Counter(path))
        for key, value in counts.items():
            if key == "start" or key == "end":
                continue
            if not cave_to_stats[key] and value > 1:
                return

        for (i, j) in transitions:
            extension = path.copy()
            if (v != i and v != j) or i == "start" or j == "start":
                continue
            ##
            if v == i:
                extension.append(j)
            if v == j:
                extension.append(i)
            build_path(extension)

    for x, y in transitions:
        if x == "start":
            path = [x, y]
            build_path(path)
        if y == "start":
            path = [y, x]
            build_path(path)

    print("PATHS = {0}".format(len(paths)))

    return


def task_24():
    s = open("data/data_task_23", "r")
    rows = s.readlines()
    s.close()

    start, cave_to_stats, transitions, end = set(), {}, set(), set()

    for row in rows:
        x, y = row.rstrip().split("-")
        x_big_cave, y_big_cave = x.isupper(), y.isupper()
        cave_to_stats[x] = x_big_cave
        cave_to_stats[y] = y_big_cave
        transitions.add((x, y))

    paths = []

    def build_path(path):
        v = path[-1]
        if v == "end":
            print("{0}".format(path))
            paths.append(path)
            return

        counts = dict(Counter(path))
        twice_visited = 0
        for key, value in counts.items():
            if key == "start" or key == "end":
                continue
            if not cave_to_stats[key] and value >= 2:
                twice_visited += value

        if twice_visited > 2:
            return

        for (i, j) in transitions:
            extension = path.copy()
            if (v != i and v != j) or i == "start" or j == "start":
                continue
            ##
            if v == i:
                extension.append(j)
            if v == j:
                extension.append(i)
            build_path(extension)

    for x, y in transitions:
        if x == "start":
            path = [x, y]
            build_path(path)
        if y == "start":
            path = [y, x]
            build_path(path)

    print("PATHS = {0}".format(len(paths)))

    return


def task_25():
    s = open("data/data_task_25", "r")
    rows = s.readlines()
    s.close()
    ##
    idx = rows.index("\n")
    positions = rows[0:idx]
    folds = rows[idx + 1:]

    positions = np.array([np.array(list(map(int, position.rstrip().split(",")))) for position in positions])
    w, h = positions[:, 0].max() + 1, positions[:, 1].max() + 1
    grid = np.zeros((h, w))
    for x, y in positions:
        grid[y, x] = 1

    mat = grid.copy()

    for fold in folds[:1]:
        dim, v = fold.replace("fold along ", "").rstrip().split("=")
        h, w = mat.shape
        v = int(v)
        if dim == "x":
            c = min(v, (w - v - 1))
            mat = mat[:, (v - c):v] + np.flip(mat[:, v + 1:], axis=1)
        if dim == "y":
            c = min(v, (h - v - 1))
            mat = mat[(v - c):v, :] + np.flip(mat[v + 1:, :], axis=0)
        mat = np.clip(mat, 0, 1)
        ##

    count = np.count_nonzero(mat)
    print("COUNT = {0}".format(count))

    return


def task_26():
    s = open("data/data_task_25", "r")
    rows = s.readlines()
    s.close()
    ##
    idx = rows.index("\n")
    positions = rows[0:idx]
    folds = rows[idx + 1:]

    positions = np.array([np.array(list(map(int, position.rstrip().split(",")))) for position in positions])
    w, h = positions[:, 0].max() + 1, positions[:, 1].max() + 1
    grid = np.zeros((2000, 2000))
    print("{0}".format((h, w)))
    for x, y in positions:
        grid[y, x] = 1

    mat = grid.copy()

    for fold in folds:
        dim, v = fold.replace("fold along ", "").rstrip().split("=")
        (h, w), v = mat.shape, int(v)
        if dim == "x":
            mat = mat[:, :v] + np.flip(mat[:, v + 1:2 * v + 1], axis=1)
        if dim == "y":
            mat = mat[:v, :] + np.flip(mat[v + 1:2 * v + 1, :], axis=0)
        mat = np.clip(mat, 0, 1)

    plt.imshow(mat)
    plt.show()
    return


def task_27():
    s = open("data/data_task_27", "r")
    rows = s.readlines()
    s.close()
    #
    polymer = rows[0].rstrip()
    rules = list(map(lambda x: x.rstrip().split(" -> "), rows[2:]))
    #
    r = polymer
    steps = 10
    for i in range(steps):
        seq = r
        w = len(seq)
        extensions = []
        for (a, b) in rules:
            for j in range(1, w):
                if r[j - 1] != a[0] or r[j] != a[1]:
                    continue
                else:
                    extensions.append((j, b))
        extensions.sort(key=lambda x: x[0])
        o = 0
        for (j, c) in extensions:
            seq = seq[:j + o] + c + seq[j + o:]
            o += 1
        if i == (steps - 1):
            counts = dict(Counter(seq))
            counts = sorted(counts.items(), key=operator.itemgetter(1))
            diff = counts[-1][1] - counts[0][1]
            print("{0} : {1} : {2}".format(i, len(seq), diff))

        r = seq
    return


def task_28():
    s = open("data/data_task_27", "r")
    rows = s.readlines()
    s.close()
    #
    polymer = rows[0].rstrip()
    rules = list(map(lambda x: x.rstrip().split(" -> "), rows[2:]))

    #

    def add_bigram(bigram, bigrams, c=1):
        if bigram in bigrams:
            bigrams[bigram] += c
        else:
            bigrams[bigram] = c

    bigrams = {}
    for i in range(1, len(polymer)):
        bigram = polymer[i - 1:i + 1]
        add_bigram(bigram, bigrams)

    counts = {}
    for b in polymer:
        if b not in counts:
            counts[b] = 1
            continue
        if b in counts:
            counts[b] += 1
            continue

    r = polymer
    steps = 40
    for i in range(steps):
        counts_ext = {}
        for a, b in rules:
            if a in bigrams:
                v = bigrams[a]
                if v <= 0:
                    continue
                bigrams[a] -= v
                x, y = a[0] + b, b + a[1]
                add_bigram(x, counts_ext, v)
                add_bigram(y, counts_ext, v)
                ##
                if b not in counts:
                    counts[b] = v
                    continue
                if b in counts:
                    counts[b] += v
                    continue
        bigrams = counts_ext
        print("{} : {}".format(i + 1, counts))
    counts = sorted(counts.items(), key=operator.itemgetter(1))
    diff = counts[-1][1] - counts[0][1]
    print("{0} : {1}".format(steps, diff))
    return


def task_29():
    s = open('data/data_task_29', 'r')
    rows = s.readlines()
    s.close()
    mat = np.array([np.array(list(map(int, list(row.rstrip())))) for row in rows])
    h, w = mat.shape
    start, end = (0, 0), (h - 1, w - 1)
    adj = [(-0, -1), (-1, -0), (-0, +1), (+1, -0)]
    #
    dist = np.ones((h, w)) * 1_000_000
    visited = np.zeros((h, w))
    #
    q = deque()
    q.append(start)
    dist[start] = 0
    visited[start] = 1

    #
    def is_ok(c):
        x, y = c
        return 0 <= x < h and 0 <= y < w

    #
    while q:
        a = q.popleft()
        for x in adj:
            b = a[0] + x[0], a[1] + x[1]
            if not is_ok(b):
                continue
            if dist[a] + mat[b] < dist[b]:
                dist[b] = dist[a] + mat[b]
                q.append(b)

    print("DISTANCE from {} to {} is {}".format(start, end, dist[end]))
    return


def task_30():
    s = open('data/data_task_29', 'r')
    rows = s.readlines()
    s.close()
    mat = np.array([np.array(list(map(int, list(row.rstrip())))) for row in rows])
    h, w = mat.shape
    ##
    tiles = np.zeros((5 * h, 5 * w))
    for i in range(5):
        if i == 0:
            tiles[i * h:(i + 1) * h, :w] = mat
        else:
            tile = tiles[(i - 1) * h:i * h, :w] + 1
            tile[tile > 9] = 1
            tiles[i * h:(i + 1) * h, :w] = tile
        for j in range(1, 5):
            tile = tiles[i * h:(i + 1) * h, (j - 1) * w:j * w] + 1
            tile[tile > 9] = 1
            tiles[i * h:(i + 1) * h, j * w:(j + 1) * w] = tile
    ##
    mat = tiles
    h, w = mat.shape
    start, end = (0, 0), (h - 1, w - 1)
    adj = [(-0, -1), (-1, -0), (-0, +1), (+1, -0)]
    #
    dist = np.ones((h, w)) * 1_000_000
    visited = np.zeros((h, w))
    #
    q = deque()
    q.append(start)
    dist[start] = 0
    visited[start] = 1

    #
    def is_ok(c):
        x, y = c
        return 0 <= x < h and 0 <= y < w

    #
    while q:
        a = q.popleft()
        for x in adj:
            b = a[0] + x[0], a[1] + x[1]
            if not is_ok(b):
                continue
            if dist[a] + mat[b] < dist[b]:
                dist[b] = dist[a] + mat[b]
                q.append(b)

    print("DISTANCE from {} to {} is {}".format(start, end, dist[end]))
    return


def task_31():
    s = open("data/data_task_31", "r")
    hexadecimal = s.readline()
    s.close()

    #
    def to_binary(i):
        as_binary = '{0:04b}'.format(int('000' + i, 16))
        return as_binary

    binary = [to_binary(i) for i in hexadecimal]
    b = ''.join(binary)

    elements, i, version_sums = [], 0, []

    def read_literal(b, i):
        literal_bits, q, c = [], i, 0
        while True:
            g_c = b[q]
            q, c = q + 1, c + 1
            bits = b[q:q + 4]
            literal_bits.append(bits)
            q, c = q + 4, c + 4
            if g_c == '0':
                break
        literal = int(''.join(literal_bits), 2)
        return q, c, literal

    def read_function(b, i, packets):
        if len(b) - i <= 6:
            return i, 0

        length, q = b[i], i + 1

        if length == '0':
            sub_length, q, j = int(b[q:q + 15], 2), q + 15, 0
            while j < sub_length:
                v, id, q = int(b[q:q + 3], 2), int(b[q + 3:q + 6], 2), q + 6
                version_sums.append(v)
                if id == 4:
                    q, c, literal = read_literal(b, q)
                    packets.append(('e', v, id, literal))
                    j += 6 + c
                else:
                    sub_packets = []
                    q, c = read_function(b, q, sub_packets)
                    packets.append(('F', v, id, sub_packets))
                    j += 6 + c
        if length == '1':
            sub_count, q, j = int(b[q:q + 11], 2), q + 11, 0
            while j < sub_count:
                v, id, q = int(b[q:q + 3], 2), int(b[q + 3:q + 6], 2), q + 6
                version_sums.append(v)
                if id == 4:
                    q, c, literal = read_literal(b, q)
                    packets.append(('e', v, id, literal))
                    j += 1
                else:
                    sub_packets = []
                    q, c = read_function(b, q, sub_packets)
                    packets.append(('F', v, id, sub_packets))
                    j += 1
        return q, q - i

    while True:
        if len(b) - i <= 6:
            break
        # [VVV] [III]
        v, id = int(b[i:i + 3], 2), int(b[i + 3:i + 6], 2)
        version_sums.append(v)
        i += 6
        if id == 4:
            # literal
            i, c, literal = read_literal(b, i)
            elements.append(('e', v, id, literal))
        else:
            # function
            packets = []
            i, c = read_function(b, i, packets)
            if packets:
                elements.append(('F', v, id, packets))
    print(elements)
    print("VERSION_SUM = {}".format(np.array(version_sums).sum()))
    return


def task_32():
    s = open("data/data_task_31", "r")
    hexadecimal = s.readline()
    s.close()

    #
    def to_binary(i):
        as_binary = '{0:04b}'.format(int('000' + i, 16))
        return as_binary

    binary = [to_binary(i) for i in hexadecimal]
    b = ''.join(binary)

    elements, i, version_sums = [], 0, []

    def evaluate(f_id, packets):
        xs = []
        for packet in packets:
            xs.append(packet[-1])
        xs = np.array(xs)
        literal = 0
        if f_id == 0:
            literal = xs.sum()
        if f_id == 1:
            literal = xs.prod()
        if f_id == 2:
            literal = xs.min()
        if f_id == 3:
            literal = xs.max()
        if f_id == 5:
            literal = 1 if xs[0] > xs[1] else 0
        if f_id == 6:
            literal = 1 if xs[0] < xs[1] else 0
        if f_id == 7:
            literal = 1 if xs[0] == xs[1] else 0
        return literal

    def read_literal(b, i):
        literal_bits, q, c = [], i, 0
        while True:
            g_c = b[q]
            q, c = q + 1, c + 1
            bits = b[q:q + 4]
            literal_bits.append(bits)
            q, c = q + 4, c + 4
            if g_c == '0':
                break
        literal = int(''.join(literal_bits), 2)
        return q, c, literal

    def read_function(b, i, packets, f_id):
        if len(b) - i <= 6:
            return i, 0, 0

        length, q, literal = b[i], i + 1, 0

        if length == '0':
            sub_length, q, j = int(b[q:q + 15], 2), q + 15, 0
            while j < sub_length:
                v, sub_f_id, q = int(b[q:q + 3], 2), int(b[q + 3:q + 6], 2), q + 6
                version_sums.append(v)
                if sub_f_id == 4:
                    q, c, literal = read_literal(b, q)
                    packets.append(('e', v, sub_f_id, literal))
                    j += 6 + c
                else:
                    sub_packets = []
                    q, c, literal = read_function(b, q, sub_packets, sub_f_id)
                    packets.append(('F', v, sub_f_id, sub_packets, literal))
                    j += 6 + c
        if length == '1':
            sub_count, q, j = int(b[q:q + 11], 2), q + 11, 0
            while j < sub_count:
                v, sub_f_id, q = int(b[q:q + 3], 2), int(b[q + 3:q + 6], 2), q + 6
                version_sums.append(v)
                if sub_f_id == 4:
                    q, c, literal = read_literal(b, q)
                    packets.append(('e', v, sub_f_id, literal))
                    j += 1
                else:
                    sub_packets = []
                    q, c, literal = read_function(b, q, sub_packets, sub_f_id)
                    packets.append(('F', v, sub_f_id, sub_packets, literal))
                    j += 1
        literal = evaluate(f_id, packets)
        return q, q - i, literal

    literal = 0
    while True:
        if len(b) - i <= 6:
            break
        # [VVV] [III]
        v, f_id = int(b[i:i + 3], 2), int(b[i + 3:i + 6], 2)
        version_sums.append(v)
        i += 6
        if f_id == 4:
            # literal
            i, c, literal = read_literal(b, i)
            elements.append(('e', v, f_id, literal))
        else:
            # function
            packets = []
            i, c, literal = read_function(b, i, packets, f_id)
            if packets:
                elements.append(('F', v, f_id, packets, literal))
    print(elements)
    print("EVALUATION = {}".format(literal))
    return


def task_33():
    s = open("data/data_task_33", "r")
    area = s.readline()
    s.close()
    #
    x, y = area.replace("target area: ", "").split(",")
    (x1, x2), (y1, y2) = list(map(int, x.replace("x=", "").split(".."))), list(map(int, y.replace("y=", "").split("..")))
    max_x, min_y = max(x1, x2), min(y1, y2)

    def has_reached(i, j):
        return x1 <= i <= x2 and y1 <= j <= y2

    def has_skipped(i, j):
        return i > max_x or j < min_y

    max_y, count = 0.0, 0

    for i in range(1, max_x):
        for j in range(1, np.abs(min_y)):
            u = [i, j]
            s, v = [0, 0], u.copy()
            local_max_y, reached = 0.0, False
            while True:
                s = s[0] + v[0], s[1] + v[1]
                ##
                if s[1] >= max_y:
                    local_max_y = max(local_max_y, s[1])
                ##
                if v[0] == 0:
                    v[0] = v[0]
                elif v[0] > 0:
                    v[0] -= 1
                elif v[0] < 0:
                    v[0] += 1
                v[1] -= 1
                if has_reached(s[0], s[1]):
                    # print("{} : {}".format(u, local_max_y))
                    reached = True
                    break
                if has_skipped(s[0], s[1]):
                    break
            if reached:
                max_y = max(max_y, local_max_y)
    print("MAX_Y = {}".format(max_y))
    return


def task_34():
    s = open("data/data_task_33", "r")
    area = s.readline()
    s.close()
    #
    x, y = area.replace("target area: ", "").split(",")
    (x1, x2), (y1, y2) = list(map(int, x.replace("x=", "").split(".."))), list(map(int, y.replace("y=", "").split("..")))
    max_x, min_y = max(x1, x2), min(y1, y2)

    def has_reached(i, j):
        return x1 <= i <= x2 and y1 <= j <= y2

    def has_skipped(i, j):
        return i > max_x or j < min_y

    max_y, count = 0.0, 0

    for i in range(1, max_x + 1):
        for j in range(-np.abs(min_y), np.abs(min_y) + 1):
            u = [i, j]
            s, v = [0, 0], u.copy()
            local_max_y, reached = 0.0, False
            while True:
                s = s[0] + v[0], s[1] + v[1]
                ##
                if s[1] >= max_y:
                    local_max_y = max(local_max_y, s[1])
                ##
                if v[0] == 0:
                    v[0] = v[0]
                elif v[0] > 0:
                    v[0] -= 1
                elif v[0] < 0:
                    v[0] += 1
                v[1] -= 1
                if has_reached(s[0], s[1]):
                    count += 1
                    # print("{} : {}".format(u, local_max_y))
                    reached = True
                    break
                if has_skipped(s[0], s[1]):
                    break
            if reached:
                max_y = max(max_y, local_max_y)
    print("MAX_Y = {} : COUNT = {}".format(max_y, count))
    return



if __name__ == "__main__":
    begin = time.time()
    run()
    runtime = time.time() - begin
    print("ADVENT in {0} s".format(runtime))
