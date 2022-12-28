import re
import unittest

class Monkey:
    def __init__(self, number, items, op, test, cond_true, cond_false):
        self.number = number
        self.items = items
        self.op = op
        self.test = test
        self.cond_true = cond_true
        self.cond_false = cond_false
        self.score = 0
#        print("id=",id)
#        print("items=",items)
#        print("op=",op, type(op))
#        print("test=",test)
#        print("cond_true=",cond_true)
#        print("cond_false=",cond_false)


def parse_input(data):
    monkeys = data.strip().split('\n\n')
    result = []
    for monkey_data in monkeys:
        monkey_lines = monkey_data.strip().split('\n')
        print("monkey_lines=",monkey_lines)
        #id = int(re.search(r'\d+', monkey_lines[0]).group())
        #or without regexp
        number = int(''.join(filter(str.isdigit, monkey_lines[0])))
        items = list(map(int,monkey_lines[1].split(':')[1].split(','))) # Starting items: 79, 98 -> [79,98]
        op = monkey_lines[2].split('=')[1]
        test = int(''.join(filter(str.isdigit, monkey_lines[3])))
        cond_true = int(''.join(filter(str.isdigit, monkey_lines[4])))
        cond_false = int(''.join(filter(str.isdigit, monkey_lines[5])))
        result.append(Monkey(number, items, op, test, cond_true, cond_false))
    return result

def make_round(monkeys, m, part, modulo=None):
    while m.items:
        monkeys[m.number].score += 1
        old = m.items.pop(0) # pop first item from the items list
        item = eval(m.op)
        #print(item)
        if part == 1:
            item = item // 3
        if part == 2:
            item = item % modulo
        if item % m.test == 0:
                next_monkey = m.cond_true
            #print("test_true")
        else:
            next_monkey = m.cond_false
            #print("test_false")
        #print("next_monkey=",next_monkey)
        monkeys[next_monkey].items.append(item)


def part1(monkeys):
    result = 0
    for round in range(20):
        for m in range(len(monkeys)):
            #print(f"round={round}, monkey={monkeys[m].number}")
            make_round(monkeys, monkeys[m], 1)
        #for monkey in monkeys:
            #print(f"after round {round} monkeys:")
            #print(f"number={monkey.number}, items={monkey.items}, test={monkey.test} score={monkey.score}")
    monkeys_sorted = sorted(monkeys, key=lambda m:m.score, reverse=True)
    result = monkeys_sorted[0].score * monkeys_sorted[1].score
    return result


def part2(monkeys):
    modulo = 1
    for m in monkeys:
        modulo *= m.test
    result = 0
    for round in range(10000):
        for m in range(len(monkeys)):
            #print(f"round={round}, monkey={monkeys[m].number}")
            make_round(monkeys, monkeys[m], 2, modulo)
        #for monkey in monkeys:
            #print(f"after round {round} monkeys:")
            #print(f"number={monkey.number}, items={monkey.items}, test={monkey.test} score={monkey.score}")
    monkeys_sorted = sorted(monkeys, key=lambda m:m.score, reverse=True)
    result = monkeys_sorted[0].score * monkeys_sorted[1].score
    return result

class TestSolution(unittest.TestCase):
    input = """
Monkey 0:
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
    If false: throw to monkey 1
"""

    def _test1(self):
        self.assertEqual(part1(parse_input(self.input)), 10605)

    def test2(self):
        self.assertEqual(part2(parse_input(self.input)), 2713310158)

if __name__ == "__main__":
    #unittest.main()
    with open("input-day-11.txt", "r") as f:
        data = f.read()
    print(part1(parse_input(data)))
    print(part2(parse_input(data)))
