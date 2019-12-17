from intcode import run_program


def main():
    program = map(int, open("day17.input", "r").read().split(","))
    scaffold = [chr(o) for o in run_program(program)]
    print("".join(scaffold))

    program = list(map(int, open("day17.input", "r").read().split(",")))
    program[0] = 2
    def by_hand_counting():
        for function in [
            "A,B,A,C,B,C,B,A,C,B",
            "L,6,R,8,R,12,L,6,L,8",
            "L,10,L,8,R,12",
            "L,8,L,10,L,6,L,6",
            "n",
        ]:
            for c in function:
                yield ord(c)
            yield ord("\n")
    for o in run_program(program, by_hand_counting):
        pass
    print(int(o))

    # Yes, I did this by hand. Judge me.
    # A L,6,R,8,R,12,L,6,L,8,
    # B L,10,L,8,R,12,
    # A L,6,R,8,R,12,L,6,L,8,
    # C L,8,L,10,L,6,L,6,
    # B L,10,L,8,R,12,
    # C L,8,L,10,L,6,L,6,
    # B L,10,L,8,R,12,
    # A L,6,R,8,R,12,L,6,L,8,
    # C L,8,L,10,L,6,L,6,
    # B L,10,L,8,R,12,


if __name__ == "__main__":
    main()
