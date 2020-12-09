import parsec as p

word = p.regex(r"[a-z]+")
number = p.regex(r"\d+").parsecmap(int)


@p.generate
def bag_parser():
    modifier = yield word
    yield p.space()
    color = yield word
    yield p.regex(r" bags?")
    return f"{modifier} {color}"


@p.generate
def line_parser():
    color = yield bag_parser
    yield p.string(" contain")
    contents = yield p.many(p.space() >> (number << p.space()) + bag_parser << p.regex(r"[,.]"))
    return (color, contents)


class Graph:
    def __init__(self):
        self.edges = {}

    @property
    def vertexes(self):
        return list(self.edges.keys())

    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, src, dest, weight):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.edges[src].append((weight, dest))

    @classmethod
    def create_with_reversed_edges(cls, other):
        g = cls()
        for vi in other.vertexes:
            for (weight, vj) in other.edges[vi]:
                g.add_edge(vj, vi, weight)
        return g

    def count_nodes_reachable_from(self, start):
        visited = {v: False for v in self.vertexes}
        stack = [v for w, v in self.edges[start]]
        total = 0
        while len(stack) > 0:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            total += 1
            for w, neighbor in self.edges[v]:
                stack.append(neighbor)
        return total


def part1():
    g = Graph()
    with open("./day7.input") as file_input:
        for line in file_input.readlines():
            color, contents = line_parser.parse(line)
            g.add_vertex(color)
            for amount, alt_color in contents:
                g.add_edge(src=color, dest=alt_color, weight=amount)
    rg = Graph.create_with_reversed_edges(g)
    print(rg.count_nodes_reachable_from("shiny gold"))


def main():
    part1()


if __name__ == "__main__":
    main()
