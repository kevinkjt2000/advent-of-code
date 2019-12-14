def solve(reaction_strings):
    reactions = parse_input(reaction_strings)
    print(reactions)
    stock = {"FUEL": 1, "ORE": 0}
    fuel = 0
    while stock.get("ORE", 0) < 1000000000000:
        modified = True
        while modified:
            modified = False
            for s in stock:
                if s == "ORE":
                    continue
                if stock[s] > 0:
                    # print("applying", s, reactions[s])
                    factor = stock[s] // reactions[s][0]
                    if factor == 0:
                        factor += 1
                        stock[s] -= reactions[s][0]
                    else:
                        stock[s] %= reactions[s][0]
                    for s_ in reactions[s][1]:
                        stock[s_] = stock.get(s_, 0) + factor*reactions[s][1][s_]
                    modified = True
                    break
        fuel += 1
        stock["FUEL"] = 1
        # print(stock["ORE"])
    print(fuel - 1)


def parse_input(reaction_strings):
    def tuple_convert(string):
        amount, name = string.strip().split(" ")
        amount = int(amount)
        return amount, name
    reactions = {}
    for rs in reaction_strings:
        inputs, output = rs.split("=>")
        output = tuple_convert(output)
        inputs = list(map(lambda s: tuple_convert(s), inputs.split(",")))
        reactions[output[1]] = (output[0], {i[1]: i[0] for i in inputs})
    return reactions


def main():
    data = open("day14.input", "r").read().strip().splitlines()
    solve(data)


if __name__ == "__main__":
    main()
