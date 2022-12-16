TEST_INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

cache = {}

def attempt(M, F, O, room, f, time_left, d=0):
    cKey = (room, tuple(O.items()), time_left)

    if cKey in cache:
        return cache[cKey]

    if time_left <= 0:
        return 0

    # try spend a minute opening the valve
    a = 0
    for neighbour in M[room]:
        a = max(
            a,
            attempt(M, F, O, neighbour, room, time_left - 1, d+1)
        )

        if O[room] == False and F[room] > 0 and time_left > 0:
            O[room] = True
            a = max(
                a,
                (F[room] * (time_left - 1)) + attempt(M, F, O, neighbour, room, time_left - 2, d+1)
            )
            O[room] = False

    cache[cKey] = a

    return a

def solve(puzzle_input):
    M = {}
    O = {}
    F = {}

    for line in puzzle_input.split("\n"):
        l, r = line.split("; ")
        l = l.split()
        v, f = l[1], l[-1]
        f = int(f.split("=")[1])

        if "valves" in r:
            ts = r[len("tunnels lead to valves "):].split(", ")
        else:
            ts = r[len("tunnel leads to valve "):].split(", ")

        M[v] = ts
        O[v] = False
        F[v] = f

    res = attempt(M, F, O, "AA", None, 30, 0)

    return res


if __name__ == "__main__":
    assert solve(TEST_INPUT) == 1651, solve(TEST_INPUT)
