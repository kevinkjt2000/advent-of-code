from queue import Queue

from more_itertools import sliding_window
import pytest


TOTAL_DISK = 70000000
UNUSED_NEEDED_FOR_UPDATE = 30000000


class Disk:
    def __init__(self):
        self.disk = {}
        self.cd("/")

    def cd(self, folder):
        if folder == "/":
            self.curdir_chain = []
        elif folder == "..":
            self.curdir_chain.pop()
        else:
            self.curdir_chain.append(folder)

        self.curdir = self.disk
        for thing in self.curdir_chain:
            self.curdir = self.curdir[thing]

    def ls(self):
        for entry in self.curdir:
            if isinstance(self.curdir[entry], int):
                yield f"{self.curdir[entry]} {entry}"
            else:
                yield f"dir {entry}"

    def mkdir(self, folder):
        if folder not in self.curdir:
            self.curdir[folder] = {}

    def touch(self, size, filename):
        self.curdir[filename] = size

    def du(self, _curdir=None):
        size = 0
        if not _curdir:
            _curdir = self.curdir
        if _curdir == {} or isinstance(_curdir, str):
            return 0
        for entry in _curdir.values():
            if isinstance(entry, int):
                size += entry
            else:
                size += self.du(entry)
        return size

    def sum_greater_than_100k(self):
        total = 0
        for size in self.iter_folder_sizes():
            if size <= 100_000:
                total += size
        return total

    def iter_folder_sizes(self):
        old_curdir_chain = self.curdir_chain
        old_curdir = self.curdir

        q = Queue()
        q.put(["/"])
        while not q.empty():
            paths = q.get()
            for p in paths:
                self.cd(p)
            yield self.du()
            for listing in self.ls():
                if listing.startswith("dir "):
                    q.put(paths + [listing[4:]])

        self.curdir_chain = old_curdir_chain
        self.curdir = old_curdir

    def find_smallest_to_free_up_space(self):
        old_curdir = self.curdir
        self.curdir = self.disk
        used_space = self.du()
        self.curdir = old_curdir

        sizes = self.iter_folder_sizes()
        minimum_size = next(sizes)
        for size in sizes:
            if (
                size < minimum_size
                and UNUSED_NEEDED_FOR_UPDATE + used_space - size <= TOTAL_DISK
            ):
                minimum_size = size
        return minimum_size


def test_example_is_solved_correctly():
    disk = parse_file("./2022/day7.example")
    assert disk.disk == {
        "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596},
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {"d.ext": 5626152, "d.log": 8033020, "j": 4060174, "k": 7214296},
    }
    disk.cd("a")
    disk.cd("e")
    assert disk.du() == 584
    disk.cd("..")
    assert disk.du() == 94_853
    disk.cd("..")
    disk.cd("d")
    assert disk.du() == 24_933_642
    disk.cd("/")
    assert disk.du() == 48_381_165

    assert disk.sum_greater_than_100k() == 95437
    assert disk.find_smallest_to_free_up_space() == 24933642


class TestDisk:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.disk = Disk()

    def test_du_works(self):
        self.disk.touch(3, "some.txt")
        assert self.disk.du() == 3

        self.disk.touch(5, "other.txt")
        assert self.disk.du() == 8

        self.disk.mkdir("blah")
        self.disk.cd("blah")
        self.disk.touch(7, "aoeu.txt")
        assert self.disk.du() == 7
        self.disk.cd("..")
        assert self.disk.du() == 15

    def test_nested_folders_work(self):
        self.disk.mkdir("first")
        self.disk.cd("first")
        self.disk.mkdir("second")
        self.disk.cd("second")
        self.disk.touch(5, "some.txt")
        assert self.disk.disk == {"first": {"second": {"some.txt": 5}}}

    def test_ls_works(self):
        assert list(self.disk.ls()) == []

    def test_mkdir_works(self):
        self.disk.mkdir("blah")
        assert list(self.disk.ls()) == ["dir blah"]

    def test_touch_works(self):
        self.disk.touch(5, "file.txt")
        assert list(self.disk.ls()) == ["5 file.txt"]

    def test_cd_works(self):
        self.disk.mkdir("blah")
        self.disk.cd("blah")
        assert list(self.disk.ls()) == []

        self.disk.cd("..")
        assert list(self.disk.ls()) == ["dir blah"]

        self.disk.cd("blah")
        self.disk.cd("/")
        assert list(self.disk.ls()) == ["dir blah"]


def parse_file(filename="./2022/day7.input"):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    disk = Disk()
    entries = []
    for line in lines:
        if line.startswith("$ "):
            entries = []
            command = line[2:]
            if command.startswith("cd"):
                folder = command[3:]
                disk.cd(folder)
            if command.startswith("ls"):
                disk.ls()
        elif line.startswith("dir "):
            disk.mkdir(folder=line[4:])
        else:
            x, filename = line.split(" ")
            disk.touch(int(x), filename)
    disk.cd("/")
    return disk


def part1():
    disk = parse_file()
    print(disk.sum_greater_than_100k())


def part2():
    disk = parse_file()
    print(disk.find_smallest_to_free_up_space())


def main():
    part2()


if __name__ == "__main__":
    main()
