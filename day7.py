data = """
Step G must be finished before step S can begin.
Step T must be finished before step Q can begin.
Step A must be finished before step B can begin.
Step H must be finished before step X can begin.
Step V must be finished before step O can begin.
Step Z must be finished before step P can begin.
Step R must be finished before step J can begin.
Step L must be finished before step Y can begin.
Step Y must be finished before step E can begin.
Step W must be finished before step X can begin.
Step X must be finished before step B can begin.
Step K must be finished before step E can begin.
Step Q must be finished before step P can begin.
Step U must be finished before step B can begin.
Step M must be finished before step O can begin.
Step P must be finished before step N can begin.
Step I must be finished before step J can begin.
Step B must be finished before step C can begin.
Step C must be finished before step O can begin.
Step J must be finished before step F can begin.
Step F must be finished before step O can begin.
Step E must be finished before step D can begin.
Step D must be finished before step N can begin.
Step N must be finished before step S can begin.
Step S must be finished before step O can begin.
Step W must be finished before step O can begin.
Step L must be finished before step P can begin.
Step N must be finished before step O can begin.
Step T must be finished before step D can begin.
Step G must be finished before step I can begin.
Step V must be finished before step X can begin.
Step B must be finished before step N can begin.
Step R must be finished before step N can begin.
Step H must be finished before step J can begin.
Step B must be finished before step S can begin.
Step P must be finished before step I can begin.
Step A must be finished before step J can begin.
Step A must be finished before step U can begin.
Step B must be finished before step D can begin.
Step T must be finished before step A can begin.
Step U must be finished before step D can begin.
Step T must be finished before step L can begin.
Step I must be finished before step E can begin.
Step R must be finished before step U can begin.
Step H must be finished before step S can begin.
Step P must be finished before step F can begin.
Step Q must be finished before step C can begin.
Step A must be finished before step P can begin.
Step X must be finished before step E can begin.
Step Q must be finished before step N can begin.
Step E must be finished before step N can begin.
Step Q must be finished before step O can begin.
Step J must be finished before step S can begin.
Step X must be finished before step P can begin.
Step K must be finished before step U can begin.
Step F must be finished before step E can begin.
Step C must be finished before step E can begin.
Step H must be finished before step K can begin.
Step W must be finished before step B can begin.
Step G must be finished before step O can begin.
Step F must be finished before step N can begin.
Step I must be finished before step D can begin.
Step G must be finished before step V can begin.
Step E must be finished before step S can begin.
Step Y must be finished before step P can begin.
Step G must be finished before step E can begin.
Step P must be finished before step J can begin.
Step U must be finished before step N can begin.
Step U must be finished before step F can begin.
Step X must be finished before step U can begin.
Step X must be finished before step C can begin.
Step R must be finished before step Q can begin.
Step Q must be finished before step E can begin.
Step Z must be finished before step E can begin.
Step X must be finished before step F can begin.
Step J must be finished before step D can begin.
Step X must be finished before step M can begin.
Step Y must be finished before step D can begin.
Step K must be finished before step J can begin.
Step Z must be finished before step J can begin.
Step M must be finished before step P can begin.
Step T must be finished before step M can begin.
Step F must be finished before step S can begin.
Step P must be finished before step S can begin.
Step X must be finished before step I can begin.
Step U must be finished before step J can begin.
Step M must be finished before step B can begin.
Step Q must be finished before step D can begin.
Step Z must be finished before step I can begin.
Step D must be finished before step S can begin.
Step J must be finished before step N can begin.
Step D must be finished before step O can begin.
Step T must be finished before step H can begin.
Step P must be finished before step D can begin.
Step M must be finished before step F can begin.
Step Y must be finished before step S can begin.
Step H must be finished before step I can begin.
Step Y must be finished before step W can begin.
Step X must be finished before step J can begin.
Step L must be finished before step W can begin.
Step G must be finished before step N can begin.
""".strip()

data2 = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".strip()

lines = data.split("\n")

relations = [(line[5], line[36]) for line in lines]

deps = {}
for (parent, child) in relations:
    if child not in deps:
        deps[child] = []
    if parent not in deps:
        deps[parent] = []
    deps[child].append(parent)
    deps[child] = sorted(deps[child])

workers = [(None, 0)] * 5
solution = ''
current_second = 0
while len(deps) > 0 or any(map(lambda w: w[0], workers)):
    for worker, w in enumerate(workers):
        # find current to work on
        if not workers[worker][0]:
            for dep in sorted(deps):
                if len(deps[dep]) == 0:
                    workers[worker] = (dep, ord(dep) - ord('A') + 61)
                    deps.pop(dep)
                    break

    for worker, w in enumerate(workers):
        workers[worker] = (workers[worker][0], workers[worker][1] - 1)

    for worker, w in enumerate(workers):
        # removal of current
        if workers[worker][0] and workers[worker][1] == 0:
            for dep in deps:
                try:
                    deps[dep].remove(workers[worker][0])
                except:
                    pass
            solution += workers[worker][0]
            workers[worker] = (None, 0)

    current_second += 1


print(solution)
print(current_second)
