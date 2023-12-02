import math
import os

fn main() {
	data := os.read_file('day1.input')!
	lines := data.split('\n')
	println(part2(lines))
}

fn extract_digit(str string) ?int {
	if str[0].is_digit() {
		return int(str[0] - `0`)
	}
	digits := ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	for i in 0 .. digits.len {
		if str.starts_with(digits[i]) {
			return i + 1
		}
	}
	return none
}

fn part2(lines []string) int {
	mut total := 0
	for line in lines {
		if line.len == 0 {
			continue
		}
		for i in 0 .. line.len {
			if num := extract_digit(line.substr(i, math.min(i + 6, line.len))) {
				total += 10 * num
				break
			}
		}
		for i := line.len - 1; i >= 0; i-- {
			if num := extract_digit(line.substr(i, line.len)) {
				total += num
				break
			}
		}
	}
	return total
}

fn part1(lines []string) int {
	mut total := 0
	for line in lines {
		mut num := 0
		for ch in line.split('') {
			if u8(ch[0]).is_digit() {
				num += 10 * int(ch[0] - `0`)
				break
			}
		}
		for ch in line.rsplit('') {
			if u8(ch[0]).is_digit() {
				num += int(ch[0] - `0`)
				break
			}
		}
		println(num)
		total += num
	}
	return total
}
