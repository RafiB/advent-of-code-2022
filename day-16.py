import sys
sys.setrecursionlimit(10000)

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

PUZZLE_INPUT = """Valve TN has flow rate=0; tunnels lead to valves IX, ZZ
Valve DS has flow rate=0; tunnels lead to valves IF, OU
Valve OP has flow rate=0; tunnels lead to valves UH, ZQ
Valve FS has flow rate=0; tunnels lead to valves IF, UH
Valve WO has flow rate=0; tunnels lead to valves IS, RW
Valve KQ has flow rate=0; tunnels lead to valves SI, WZ
Valve IX has flow rate=0; tunnels lead to valves IF, TN
Valve OU has flow rate=0; tunnels lead to valves EB, DS
Valve ZZ has flow rate=10; tunnels lead to valves II, GR, HA, BO, TN
Valve OW has flow rate=0; tunnels lead to valves RI, IS
Valve DV has flow rate=0; tunnels lead to valves FR, MT
Valve ZK has flow rate=0; tunnels lead to valves WG, VE
Valve XB has flow rate=0; tunnels lead to valves WG, HM
Valve XC has flow rate=0; tunnels lead to valves IS, MT
Valve KO has flow rate=0; tunnels lead to valves NH, AA
Valve RN has flow rate=0; tunnels lead to valves AA, MT
Valve ZQ has flow rate=5; tunnels lead to valves MF, LK, OP
Valve MF has flow rate=0; tunnels lead to valves ZQ, BH
Valve HA has flow rate=0; tunnels lead to valves LK, ZZ
Valve GB has flow rate=0; tunnels lead to valves KZ, RW
Valve KZ has flow rate=24; tunnels lead to valves GB, RI
Valve TC has flow rate=0; tunnels lead to valves SI, AA
Valve II has flow rate=0; tunnels lead to valves SI, ZZ
Valve EZ has flow rate=0; tunnels lead to valves DF, MT
Valve LK has flow rate=0; tunnels lead to valves HA, ZQ
Valve DU has flow rate=0; tunnels lead to valves NH, IU
Valve MT has flow rate=3; tunnels lead to valves EZ, XC, RN, DV, RU
Valve GR has flow rate=0; tunnels lead to valves SX, ZZ
Valve SX has flow rate=0; tunnels lead to valves UH, GR
Valve BO has flow rate=0; tunnels lead to valves ZZ, AO
Valve WG has flow rate=16; tunnels lead to valves FR, MX, XB, ZK
Valve IP has flow rate=8; tunnels lead to valves HM, RU, WZ, IU
Valve RI has flow rate=0; tunnels lead to valves OW, KZ
Valve NP has flow rate=0; tunnels lead to valves WN, EB
Valve IF has flow rate=19; tunnels lead to valves IX, DS, VX, FS
Valve AA has flow rate=0; tunnels lead to valves RN, KO, TC, MX
Valve IS has flow rate=15; tunnels lead to valves OW, WO, XC
Valve BH has flow rate=11; tunnel leads to valve MF
Valve SI has flow rate=4; tunnels lead to valves KQ, II, TC
Valve WN has flow rate=0; tunnels lead to valves UH, NP
Valve RW has flow rate=18; tunnels lead to valves WO, GB
Valve DF has flow rate=0; tunnels lead to valves NH, EZ
Valve WZ has flow rate=0; tunnels lead to valves KQ, IP
Valve HM has flow rate=0; tunnels lead to valves XB, IP
Valve VX has flow rate=0; tunnels lead to valves AO, IF
Valve MX has flow rate=0; tunnels lead to valves AA, WG
Valve NH has flow rate=13; tunnels lead to valves VE, KO, DU, DF
Valve RU has flow rate=0; tunnels lead to valves MT, IP
Valve IU has flow rate=0; tunnels lead to valves IP, DU
Valve VE has flow rate=0; tunnels lead to valves ZK, NH
Valve FR has flow rate=0; tunnels lead to valves WG, DV
Valve AO has flow rate=21; tunnels lead to valves BO, VX
Valve EB has flow rate=22; tunnels lead to valves OU, NP
Valve UH has flow rate=12; tunnels lead to valves WN, OP, SX, FS"""

cache = {}

def attempt(M, F, O, room, time_left, d):
    cKey = (room, tuple(O.items()), time_left, d)

    if cKey in cache:
        return cache[cKey]

    if time_left <= 0:
        if d == 0:
            return attempt(M, F, O, "AA", 26, 1)
        return 0

    # try spend a minute opening the valve
    a = 0
    for neighbour in M[room]:
        a = max(
            a,
            attempt(M, F, O, neighbour, time_left - 1, d)
        )

        if O[room] == False and F[room] > 0 and time_left > 0:
            O[room] = True
            a = max(
                a,
                (F[room] * (time_left - 1)) + attempt(M, F, O, neighbour, time_left - 2, d)
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

    res = attempt(M, F, O, "AA", 26, 0)

    return res


if __name__ == "__main__":
    assert solve(TEST_INPUT) == 1707, solve(TEST_INPUT)
    print(solve(PUZZLE_INPUT))
