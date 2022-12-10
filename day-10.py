TEST_INPUT = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

PUZZLE_INPUT = """noop
noop
addx 5
noop
noop
addx 6
addx 4
addx -4
addx 4
addx -6
addx 11
addx -1
addx 2
addx 4
addx 3
noop
addx 2
addx -30
addx 2
addx 33
noop
addx -37
noop
noop
noop
addx 3
addx 2
addx 5
addx 20
addx 7
addx -24
addx 2
noop
addx 7
addx -2
addx -6
addx 13
addx 3
addx -2
addx 2
noop
addx -5
addx 10
addx 5
addx -39
addx 1
addx 5
noop
addx 3
noop
addx -5
addx 10
addx -2
addx 2
noop
noop
addx 7
noop
noop
noop
noop
addx 3
noop
addx 3
addx 2
addx 8
addx -1
addx -20
addx 21
addx -38
addx 5
addx 2
noop
noop
noop
addx 8
noop
noop
addx -2
addx 2
addx -7
addx 14
addx 5
noop
noop
noop
addx -16
addx 17
addx 2
addx -12
addx 19
noop
noop
addx -37
noop
noop
noop
addx 3
addx 2
addx 2
addx 5
addx 20
addx -19
addx 2
noop
noop
noop
addx 5
addx 19
addx -12
addx 3
addx -2
addx 2
addx -18
addx 25
addx -14
addx -22
addx 1
noop
noop
noop
addx 3
addx 5
addx -4
addx 7
addx 4
noop
addx 1
noop
noop
addx 2
addx -6
addx 15
addx -1
addx 4
noop
noop
addx 1
addx 4
addx -33
noop
addx 21
noop"""


def solve(puzzle_input):
    V = 1
    res = 0
    cycle = 0
    lines = puzzle_input.split("\n")
    i = 0
    wake = None
    to_add = None
    while i < len(lines):
        if cycle == 20 or (cycle > 20 and (cycle-20) % 40 == 0):
            res += cycle * V

        if wake != None and cycle < wake:
            cycle += 1
            continue
        if to_add != None:
            V += to_add
            to_add = None

        line = lines[i]
        i += 1

        if line == "noop":
            wake = cycle + 1
        else:
            _, d = line.split(" ")
            d = int(d)
            to_add = d
            wake = cycle + 2
        cycle += 1
    return res


if __name__ == "__main__":
    assert solve(TEST_INPUT) == 13140, solve(TEST_INPUT)
    print(solve(PUZZLE_INPUT))
