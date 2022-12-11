TEST_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

PUZZLE_INPUT = """Monkey 0:
  Starting items: 97, 81, 57, 57, 91, 61
  Operation: new = old * 7
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 1:
  Starting items: 88, 62, 68, 90
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 2

Monkey 2:
  Starting items: 74, 87
  Operation: new = old + 2
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 3:
  Starting items: 53, 81, 60, 87, 90, 99, 75
  Operation: new = old + 1
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 4:
  Starting items: 57
  Operation: new = old + 6
  Test: divisible by 13
    If true: throw to monkey 7
    If false: throw to monkey 0

Monkey 5:
  Starting items: 54, 84, 91, 55, 59, 72, 75, 70
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 3

Monkey 6:
  Starting items: 95, 79, 79, 68, 78
  Operation: new = old + 3
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 7:
  Starting items: 61, 97, 67
  Operation: new = old + 4
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 5"""


class Add(object):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def on(self, n):
        l = n if self.lhs == "old" else self.lhs
        r = n if self.rhs == "old" else self.rhs
        return l + r


class Multiply(object):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def on(self, n):
        l = n if self.lhs == "old" else self.lhs
        r = n if self.rhs == "old" else self.rhs
        return l * r


def solve(puzzle_input):
    monkeys = {}
    handled = {}
    cm = 1

    for monkey_def in puzzle_input.split("\n\n"):
        def_lines = monkey_def.split("\n")
        _, i = def_lines[0][:-1].split(' ')
        i = int(i)

        _, items = def_lines[1].split(": ")
        items = [int(i) for i in items.split(", ")]

        _, o = def_lines[2].split(" = ")
        [lhs, op, rhs] = o.split(" ")
        if lhs != "old":
            lhs = int(lhs)
        if rhs != "old":
            rhs = int(rhs)
        if op == "+":
            op = Add(lhs, rhs)
        else:
            op = Multiply(lhs, rhs)

        test = int(def_lines[3].split(" ")[-1])
        cm *= test

        yes_i = int(def_lines[4].split(" ")[-1])
        no_i = int(def_lines[5].split(" ")[-1])

        # print(i, items, lhs, op, rhs, test, yes_i, no_i)

        monkeys[i] = (items, op, test, yes_i, no_i)
        handled[i] = 0

    for i in range(10000):
        if i % 20 == 0:
            print(i, handled)
        for i in range(len(monkeys)):
            instr = monkeys[i]

            for item in instr[0]:
                handled[i] += 1
                worry_level = instr[1].on(item)
                if worry_level % instr[2] == 0:
                    dest = instr[3]
                else:
                    dest = instr[4]
                (t_items, t_op, t_test, t_yes_i, t_no_i) = monkeys[dest]
                monkeys[dest] = (t_items + [worry_level % cm], t_op, t_test, t_yes_i, t_no_i)

            monkeys[i] = ([], instr[1], instr[2], instr[3], instr[4])

    [a, b] = list(sorted(handled.values()))[-2:]
    return a * b


if __name__ == "__main__":
    assert solve(TEST_INPUT) == 2713310158, solve(TEST_INPUT)
    print(solve(PUZZLE_INPUT))
