TEST_INPUT = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

PUZZLE_INPUT = """Sensor at x=2332081, y=2640840: closest beacon is at x=2094728, y=2887414
Sensor at x=3048293, y=3598671: closest beacon is at x=3872908, y=3598272
Sensor at x=2574256, y=3973583: closest beacon is at x=2520711, y=4005929
Sensor at x=3011471, y=2514567: closest beacon is at x=2999559, y=2558817
Sensor at x=3718881, y=2593817: closest beacon is at x=2999559, y=2558817
Sensor at x=2388052, y=2201955: closest beacon is at x=2163809, y=1961540
Sensor at x=3783125, y=3897169: closest beacon is at x=3872908, y=3598272
Sensor at x=1864613, y=3918152: closest beacon is at x=2520711, y=4005929
Sensor at x=2850099, y=689863: closest beacon is at x=3231146, y=2000000
Sensor at x=3431652, y=2328669: closest beacon is at x=3231146, y=2000000
Sensor at x=3480248, y=3999492: closest beacon is at x=3872908, y=3598272
Sensor at x=455409, y=3347614: closest beacon is at x=-399822, y=4026621
Sensor at x=2451938, y=2950107: closest beacon is at x=2094728, y=2887414
Sensor at x=1917790, y=3194437: closest beacon is at x=2094728, y=2887414
Sensor at x=3947393, y=3625984: closest beacon is at x=3872908, y=3598272
Sensor at x=1615064, y=2655330: closest beacon is at x=2094728, y=2887414
Sensor at x=3630338, y=1977851: closest beacon is at x=3231146, y=2000000
Sensor at x=3878266, y=3019867: closest beacon is at x=3872908, y=3598272
Sensor at x=2837803, y=2395749: closest beacon is at x=2999559, y=2558817
Sensor at x=3979396, y=3697962: closest beacon is at x=3872908, y=3598272
Sensor at x=109399, y=250528: closest beacon is at x=929496, y=-688981
Sensor at x=2401381, y=3518884: closest beacon is at x=2520711, y=4005929
Sensor at x=3962391, y=71053: closest beacon is at x=5368730, y=-488735
Sensor at x=1751119, y=97658: closest beacon is at x=929496, y=-688981
Sensor at x=2932155, y=2967347: closest beacon is at x=2999559, y=2558817
Sensor at x=3326630, y=2845463: closest beacon is at x=2999559, y=2558817
Sensor at x=3959042, y=1734156: closest beacon is at x=3231146, y=2000000
Sensor at x=675279, y=1463916: closest beacon is at x=2163809, y=1961540
Sensor at x=3989603, y=3500749: closest beacon is at x=3872908, y=3598272
Sensor at x=1963470, y=2288355: closest beacon is at x=2163809, y=1961540"""

def solve(puzzle_input, solve_line):
    CLOSEST_BEACONS = {}
    for line in puzzle_input.split("\n"):
        l, r = line.split(": ")
        l = l.split(" ")[-2:]
        r = r.split(" ")[-2:]
        sx, sy = l[0], int(l[1].split("=")[1])
        sx = int(sx[:-1].split("=")[1])

        bx, by = r[0], int(r[1].split("=")[1])
        bx = int(bx[:-1].split("=")[1])

        CLOSEST_BEACONS[(sx, sy)] = (bx, by)

    CANNOT_BE = set()
    for s in CLOSEST_BEACONS:
        b = CLOSEST_BEACONS[s]
        manhattan_distance = abs(s[0] - b[0]) + abs(s[1] - b[1])

        x, y = s
        if abs(y - solve_line) > manhattan_distance:
            continue

        for dx in range(manhattan_distance - abs(y - solve_line) + 1):
            assert 1 <= abs(dx) + abs(y - solve_line) and abs(dx) + abs(y - solve_line) <= manhattan_distance
            CANNOT_BE.add(s[0] - dx)
            CANNOT_BE.add(s[0] + dx)


    return len(CANNOT_BE) - 1


if __name__ == "__main__":
    assert solve(TEST_INPUT, 10) == 26, solve(TEST_INPUT, 10)
    print(solve(PUZZLE_INPUT, 2000000))
