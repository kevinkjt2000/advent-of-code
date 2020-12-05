import re

hcl_pattern = re.compile("^#[0-9a-f]{6}$")
pid_pattern = re.compile("^[0-9]{9}$")
hgt_pattern = re.compile("^[0-9]{2,3}(cm|in)$")


def parse_input_as_stream_of_records():
    with open("./day4.input") as file_input:
        record = ""
        for line in file_input.readlines():
            if line.strip():
                record += " " + line.strip()
            else:
                yield {k: v for k, v in [kv.split(":") for kv in record.split(" ") if kv]}
                record = ""
        yield {k: v for k, v in [kv.split(":") for kv in record.split(" ") if kv]}


def is_valid_record(record, part2_enabled=False) -> bool:
    if part2_enabled:
        return (
            all((key in record) for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
            and int(record["byr"]) in range(1920, 2003)
            and int(record["iyr"]) in range(2010, 2021)
            and int(record["eyr"]) in range(2020, 2031)
            and bool(hcl_pattern.match(record["hcl"]))
            and record["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            and bool(pid_pattern.match(record["pid"]))
            and bool(hgt_pattern.match(record["hgt"]))
            and (
                (record["hgt"][-2:] == "cm" and int(record["hgt"][:-2]) in range(150, 194))
                or (record["hgt"][-2:] == "in" and int(record["hgt"][:-2]) in range(59, 77))
            )
        )
    else:
        return all((key in record) for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def part1():
    total_valid = 0
    for record in parse_input_as_stream_of_records():
        if is_valid_record(record):
            total_valid += 1
    return total_valid


def part2():
    total_valid = 0
    for record in parse_input_as_stream_of_records():
        if is_valid_record(record, part2_enabled=True):
            total_valid += 1
    return total_valid


def main():
    print(part2())


if __name__ == "__main__":
    main()
